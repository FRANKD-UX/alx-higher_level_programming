#!/bin/bash
# Fetches the body of a 200 status response
curl -sL -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -sL "$1"
