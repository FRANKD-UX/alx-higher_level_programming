#!/bin/bash
# Fetches the body of a response only for 200 status code
curl -s "$1" | grep -E '^HTTP/.* 200' | cut -d ' ' -f 4-
