#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers from a list.

    Args:
        my_list (list): The input list of integers.
    
    Returns:
        int: The sum of unique integers from the list.
    """
    # Use set to eliminate duplicates, then sum the unique values
    return sum(set(my_list))
