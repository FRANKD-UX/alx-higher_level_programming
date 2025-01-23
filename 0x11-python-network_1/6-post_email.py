#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter"""

import requests
import sys


def post_email(url, email):
    """Sends a POST request and displays the response body"""
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
