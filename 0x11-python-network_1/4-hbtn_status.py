#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using the requests package"""

import requests


def fetch_status():
    """Fetches and displays the status of a URL"""
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)


if __name__ == "__main__":
    fetch_status()
