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


# Example usage
if __name__ == "__main__":
    a_dictionary = {'a': 'a', 'b': 'b', 'c': 'c'}
    simple_delete(a_dictionary, 'b')
    print(a_dictionary)  # Output: {'a': 'a', 'c': 'c'}

    simple_delete(a_dictionary, 'd')  # Trying to delete a non-existing key
    print(a_dictionary)  # Output: {'a': 'a', 'c': 'c'}
