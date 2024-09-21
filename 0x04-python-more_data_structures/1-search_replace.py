#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a list with a new element.

    Args:
        my_list (list): The initial list.
        search: The element to replace.
        replace: The new element to replace the search element with.

    Returns:
        list: A new list with the replaced elements.
    """
    # Use list comprehension to create a new list with replacements
    return [replace if element == search else element for element in my_list]
