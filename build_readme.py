import os
import re
import requests
from datetime import datetime, timezone

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
README_PATH = "README.md"
REPO_COUNT = 5

def fetch_recent_repos():
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    params = {
        "sort": "pushed",
        "direction": "desc",
        "per_page": REPO_COUNT,
        "type": "owner",
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def format_repos(repos):
    now = datetime.now(timezone.utc)
    lines = []
    for repo in repos:
        name        = repo["name"]
        description = repo.get("description") or "—"
        pushed_at   = repo["pushed_at"]          # e.g. "2024-03-01T12:34:56Z"
        url         = repo["html_url"]
        language    = repo.get("language") or "—"
        stars       = repo.get("stargazers_count", 0)

        # Calculate days ago
        pushed_dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        delta = (now - pushed_dt).days
        if delta == 0:
            age = "today"
        elif delta == 1:
            age = "1 day ago"
        else:
            age = f"{delta} days ago"

        lines.append(
            f"  [{name}]({url})"
            f"  ·  {description}"
            f"  ·  {language}"
            f"  ·  ⭐ {stars}"
            f"  ·  pushed {age}"
        )
    return "\n".join(lines)

def update_readme(content):
    readme_path = README_PATH
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = (
        f"<!-- recent_activity starts -->\n"
        f"```\n"
        f"[updated: {updated_at}]\n\n"
        f"{content}\n"
        f"```\n"
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
