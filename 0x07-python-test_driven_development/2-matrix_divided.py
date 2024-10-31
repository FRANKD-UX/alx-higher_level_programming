#!/usr/bin/python3
"""This module contains a function to divide all elements of
a matrix by a given number."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int, float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with the divided values rounded to 2 decimal places.
    """

    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements in the matrix are lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    # Get the length of the first row
    row_length = len(matrix[0])

    # Check if all rows have the same length
    for row in matrix:
        if len(row) != row_length:
            raise TypeError
        ("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError
            ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
