#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list and saves them
to a JSON file.
"""

import sys
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# File to store the list in JSON format
filename = "add_item.json"

# Check if the file exists and load existing data; otherwise,
start with an empty list
if Path(filename).is_file():
    data = load_from_json_file(filename)
else:
    data = []

# Append command-line arguments (excluding the script name itself) to the list
data.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(data, filename)
