#!/bin/bash
# Makes a request to /catch_me and displays the response body
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
