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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attributes to retrieve.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary with new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
