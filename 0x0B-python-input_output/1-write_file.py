#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 encoded text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file and
    returns the character count.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
