#!/usr/bin/python3
"""This module contains a function to print a name."""


def say_my_name(first_name, last_name=""):
    """Prints a greeting with the provided first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or
                        last_name must be a string")

    print(f"My name is {first_name} {last_name}")
