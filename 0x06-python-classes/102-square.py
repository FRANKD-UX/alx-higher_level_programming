#!usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    def __init__(self, size=0):
        self.size = size  # Use the property setter to initialize size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if the area of two squares is equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if the area of two squares is not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of this square is less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of this square is less than or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of this square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of this square is greater than or equal to the other."""
        return self.area() >= other.area()
