#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of the response"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """Fetches and displays the body of the response"""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
