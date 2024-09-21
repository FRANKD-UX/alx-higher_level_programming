#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be deleted.

    Returns:
        None
    """
    a_dictionary.pop(key, None)


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


# Example usage
if __name__ == "__main__":
    a_dictionary = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}

    # Delete a key and print the dictionary
    simple_delete(a_dictionary, 'a')
    print_sorted_dictionary(a_dictionary)  # Output: b: b, c: c, d: d, e: e

    simple_delete(a_dictionary, 'e')
    print_sorted_dictionary(a_dictionary)  # Output: b: b, c: c, d: d

    simple_delete(a_dictionary, 'f')  # Attempt to delete a non-existing key
    print_sorted_dictionary(a_dictionary)  # Output: b: b, c: c, d: d
