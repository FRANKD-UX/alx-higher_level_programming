#!/usr/bin/python3
"""Sends a request to a given URL and displays the value of the X-Request-Id variable in the response header"""

import requests
import sys


def fetch_header_value(url):
    """Fetches and displays the X-Request-Id header value"""
    response = requests.get(url)
    header_value = response.headers.get('X-Request-Id')
    print(header_value)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header_value(url)
