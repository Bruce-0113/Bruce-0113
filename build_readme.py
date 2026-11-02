import html
import os
import re
import requests

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
README_PATH = "README.md"
REPO_COUNT = 5
# Repos pushed daily by bots would always sit at the top of the list
EXCLUDE_REPOS = {GITHUB_USERNAME, "ai-paper-tracker"}

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
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    repos = [
        repo for repo in response.json()
        if not repo["fork"]
        and not repo["archived"]
        and repo["name"] not in EXCLUDE_REPOS
    ]
    return repos[:REPO_COUNT]

def format_repos(repos):
    lines = []
    for repo in repos:
        name        = html.escape(repo["name"])
        description = html.escape(repo.get("description") or "—")
        pushed_at   = repo["pushed_at"]          # e.g. "2024-03-01T12:34:56Z"
        url         = repo["html_url"]
        language    = repo.get("language") or "—"
        stars       = repo.get("stargazers_count", 0)

        # Absolute date, so the README only changes when a repo is pushed
        pushed_on = pushed_at[:10]

        # Markdown links don't render inside code blocks; <pre> keeps the
        # terminal look while letting <a> tags through
        lines.append(
            f'  <a href="{url}">{name}</a>'
            f"  ·  {description}"
            f"  ·  {language}"
            f"  ·  ⭐ {stars}"
            f"  ·  pushed {pushed_on}"
        )
    return "\n".join(lines)

def update_readme(content):
    readme_path = README_PATH
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    block = (
        f"<!-- recent_activity starts -->\n"
        f"<pre>\n"
        f"{content}\n"
        f"</pre>\n"
        f"<!-- recent_activity ends -->"
    )

    new_readme = re.sub(
        r"<!-- recent_activity starts -->.*?<!-- recent_activity ends -->",
        block,
        readme,
        flags=re.DOTALL,
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)

    print("README updated.")

if __name__ == "__main__":
    repos = fetch_recent_repos()
    formatted = format_repos(repos)
    update_readme(formatted)
