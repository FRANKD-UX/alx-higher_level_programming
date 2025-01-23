#!/bin/bash
# Sends a GET request to the URL and displays the body of the response if status code is 200
response=$(curl -s -w "%{http_code}" -o response.txt "$1")
if [ "$response" -eq 200 ]; then
  cat response.txt
fi
