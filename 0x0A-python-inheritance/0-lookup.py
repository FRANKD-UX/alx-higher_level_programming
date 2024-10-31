#!/usr/bin/python3
"""
Module for the lookup function.
The lookup function retrieves the list of available
attributes and methods for a given object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attributes and methods available for the object.
    """
    return dir(obj)
