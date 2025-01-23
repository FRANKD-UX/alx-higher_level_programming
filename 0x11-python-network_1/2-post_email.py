#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """Sends a POST request and displays the response body"""
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
