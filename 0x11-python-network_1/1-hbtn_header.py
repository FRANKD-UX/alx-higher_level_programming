#!/usr/bin/python3
"""Fetches the value of the X-Request-Id header variable from a given URL"""

import urllib.request
import sys


def fetch_header_value(url):
    """Fetches and displays the X-Request-Id header value"""
    with urllib.request.urlopen(url) as response:
        header_value = response.headers.get('X-Request-Id')
        print(header_value)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header_value(url)
