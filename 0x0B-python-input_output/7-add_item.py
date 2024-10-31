#!/usr/bin/python3
"""
This script adds all command-line arguments to a list and saves
it to a JSON file.

The list is stored in add_item.json and is updated each time the script is run.
"""

import sys
from pathlib import Path

# Import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename for the JSON file
filename = "add_item.json"

# Initialize the list by loading existing data or creating a new
# list if the file doesn't exist


if Path(filename).is_file():
    data = load_from_json_file(filename)
else:
    data = []

# Add command-line arguments (excluding the script name) to the list
data.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(data, filename)
