#!/bin/bash
# Sends a GET request to the URL and displays the body of the response if status code is 200
curl -sL "$1" | grep -q "HTTP/1.1 200 OK" && curl -sL "$1"
