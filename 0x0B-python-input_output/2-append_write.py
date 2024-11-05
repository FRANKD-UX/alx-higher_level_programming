#!/usr/bin/python3
"""
This module provides a function to append a string to a
UTF-8 encoded text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 encoded text file and
    returns the character count.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file. Defaults to an
        empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
