#!/bin/bash
# Sends a JSON POST request with the contents of a file and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
