#!/usr/bin/python3
"""
This module provides a function to convert a
JSON string back to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
