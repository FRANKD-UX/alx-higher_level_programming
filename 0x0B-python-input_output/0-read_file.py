#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a
UTF-8 encoded text file.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
