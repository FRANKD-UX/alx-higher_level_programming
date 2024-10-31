#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from list.
The MyList class includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of list with an additional method to print the list
    in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list's elements in ascending sorted order.
        Assumes all elements are integers.
        """
        print(sorted(self))
