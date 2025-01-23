#!/usr/bin/python3
"""Defines a function to find a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Finds a peak element in the list.
    
    A peak is an element that is greater than or equal to its neighbors.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        # Compare middle element with its neighbor on the right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1  # Move to the right half
        else:
            high = mid  # Move to the left half or stay at mid

    # low and high converge to the peak
    return list_of_integers[low]
