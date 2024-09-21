#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in the dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be updated or added.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with keys sorted in alphabetical order.

    Args:
        a_dictionary (dict): The input dictionary with string keys.

    Returns:
        None
    """
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
