#!/usr/bin/python3
"""Uses the GitHub API to display the user's id"""

import requests
import sys


def get_github_id(username, token):
    """Fetches and displays the GitHub user id"""
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    json_response = response.json()
    print(json_response.get('id', 'None'))


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
