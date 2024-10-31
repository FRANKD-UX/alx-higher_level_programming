#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: The first number, must be an integer or a float.
        b: The second number, must be an integer or a float. Default is 98.

    Returns:
        The sum of a and b after both are cast to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers in case of floats
    a = int(a)
    b = int(b)

    return a + b
