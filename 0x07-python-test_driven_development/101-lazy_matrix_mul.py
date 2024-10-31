#!/usr/bin/python3
""" This module defines a function to multiply two matrices using NumPy. """

import numpy as np


def lazy_matrix_mul(ma, mb):
    # Check if inputs are lists
    if not isinstance(ma, list) or not isinstance(mb, list):
        raise TypeError("Inputs must be lists")

    # Check if inputs are not empty
    if len(ma) == 0 or len(mb) == 0:
        raise ValueError("Inputs cannot be empty")

    # Check if all rows in ma are of the same size
    row_length = len(ma[0])
    for row in ma:
        if len(row) != row_length:
            raise TypeError("Each row of m_a must be of the same size")

    # Check if all rows in mb are of the same size
    row_length = len(mb[0])
    for row in mb:
        if len(row) != row_length:
            raise TypeError("Each row of m_b must be of the same size")

    # Check if all elements in ma are numbers
    for row in ma:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    # Check if all elements in mb are numbers
    for row in mb:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if dimensions are aligned for multiplication
    if len(ma[0]) != len(mb):
        raise ValueError("ma and mb can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(mb[0]))] for _ in range(len(ma))]
    for i in range(len(ma)):
        for j in range(len(mb[0])):
            for k in range(len(mb)):
                result[i][j] += ma[i][k] * mb[k][j]
    return result
