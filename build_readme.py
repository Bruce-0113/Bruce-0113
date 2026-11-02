import html
import os
import re
import requests
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
README_PATH = "README.md"
REPO_COUNT = 5
# Repos pushed daily by bots would always sit at the top of the list
EXCLUDE_REPOS = {GITHUB_USERNAME, "ai-paper-tracker"}
SITE_URL = "https://bruce-notes.s24578111.workers.dev"
POST_COUNT = 5
TIMEOUT = 30

def fetch_recent_repos():
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    params = {
        "sort": "pushed",
        "direction": "desc",
        "per_page": 30,
        "type": "owner",
    }
    response = requests.get(url, headers=headers, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    repos = [
        repo for repo in response.json()
        if not repo["fork"]
        and not repo["archived"]
        and repo["name"] not in EXCLUDE_REPOS
    ]
    return repos[:REPO_COUNT]

def fetch_latest_posts():
    response = requests.get(f"{SITE_URL}/rss.xml", timeout=TIMEOUT)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    posts = []
    for item in root.iter("item"):
        # Feed mixes posts, notes, readings and projects; keep long-form posts only
        categories = [c.text for c in item.findall("category")]
        if "posts" not in categories:
            continue
        posts.append({
            "title"    : item.findtext("title"),
            "url"      : item.findtext("link"),
            "published": parsedate_to_datetime(item.findtext("pubDate")),
        })
    posts.sort(key=lambda post: post["published"], reverse=True)
    return posts[:POST_COUNT]

def format_repos(repos):
    width = max((len(repo["name"]) for repo in repos), default=0)
    lines = []
    for repo in repos:
        name        = html.escape(repo["name"])
        pushed_at   = repo["pushed_at"]          # e.g. "2024-03-01T12:34:56Z"
        url         = repo["html_url"]
        language    = repo.get("language") or "—"
        padding     = " " * (width - len(repo["name"]))

        # Absolute date, so the README only changes when a repo is pushed
        pushed_on = pushed_at[:10]

        # Markdown links don't render inside code blocks; <pre> keeps the
        # terminal look while letting <a> tags through
        lines.append(
            f"  {pushed_on}"
            f'  <a href="{url}">{name}</a>{padding}'
            f"  {language}"
        )
    return "\n".join(lines)

def format_posts(posts):
    lines = []
    for post in posts:
        title     = html.escape(post["title"])
        url       = html.escape(post["url"])
        published = post["published"].strftime("%Y-%m-%d")
        lines.append(f'  {published}  <a href="{url}">{title}</a>')
    lines.append(f'\n  → <a href="{SITE_URL}/">all posts, notes &amp; readings (zh-TW)</a>')
    return "\n".join(lines)

def update_readme(sections):
    readme_path = README_PATH
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    for marker, content in sections.items():
        block = (
            f"<!-- {marker} starts -->\n"
            f"<pre>\n"
            f"{content}\n"
            f"</pre>\n"
            f"<!-- {marker} ends -->"
        )
        # Pass a function so backslashes in titles aren't read as escapes
        readme = re.sub(
            rf"<!-- {marker} starts -->.*?<!-- {marker} ends -->",
            lambda _: block,
            readme,
            flags=re.DOTALL,
        )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print("README updated.")

if __name__ == "__main__":
    update_readme({
        "latest_posts"   : format_posts(fetch_latest_posts()),
        "recent_activity": format_repos(fetch_recent_repos()),
    })
