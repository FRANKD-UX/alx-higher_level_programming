#!/usr/bin/python3
"""Lists 10 commits from a given repository
by a given user using the GitHub API"""

import requests
import sys


def list_commits(repo, owner):
    """Fetches and displays 10 commits from the specified repository"""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repo, owner)
