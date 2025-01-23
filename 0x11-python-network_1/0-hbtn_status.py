#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

import urllib.request

def fetch_status():
    """Fetches and displays the status of a URL"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))

if __name__ == "__main__":
    fetch_status()
