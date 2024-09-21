#!/usr/bin/python3
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
