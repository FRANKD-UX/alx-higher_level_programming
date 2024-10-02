#!/usr/bin/python3
"""
This module defines a class MagicClass.
"""

import math


class MagicClass:
    """
    This class represents a circle with a given radius.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a radius.
        Args:
            radius (int, float): The radius of the circle.
        Raises:
            TypeError: If radius is not a number.
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self._MagicClass__radius
