#!/usr/bin/python3
"""
This module provides a function to convert an object
to its JSON representation.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
