#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        return self.__dict__
