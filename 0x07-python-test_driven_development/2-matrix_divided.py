#!/usr/bin/python3
"""
This module contains a function that divides all elements of a
matrix by a specified number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a specified divisor.

    Args:
        matrix (list of list of int/float): A matrix (list of lists)
        of integers or floats.
        div (int/float): The number by which to divide each element
        of the matrix.

    Returns:
        list of list of float: A new matrix containing the results
        of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Validate the matrix
    if not isinstance(matrix, list)
    or not all(isinstance(row, list) for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    # Validate the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
