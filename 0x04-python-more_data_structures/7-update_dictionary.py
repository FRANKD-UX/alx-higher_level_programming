#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in the dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be updated or added.
        value: The value associated with the key.

    Returns:
        None
    """
    # Update or add the key/value pair in the dictionary
    a_dictionary[key] = value
