#!/usr/bin/python3
"""Sends a request to a given URL and displays
the body of the response or an error code"""

import requests
import sys


def fetch_url(url):
    """Fetches and displays the body of the 
    response or an error code"""
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
