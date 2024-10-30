#!/usr/bin/python3
"""
This module defines a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
     Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        obj: The object represented by the JSON string.
    """
    with open(filename, 'r') as file:
        return json.load(file)
