#!/bin/bash
# Sends a GET request to the URL, follows redirects, and displays the body of the response if status code is 200
curl -sL "$1" | grep -o 'HTTP/1.1 [0-9]*' | grep -q '200' && curl -sL "$1"
