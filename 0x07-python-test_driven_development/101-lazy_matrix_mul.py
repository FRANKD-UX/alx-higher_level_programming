#!/usr/bin/python3
"""
This module defines a function to multiply two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, or if they contain non-numeric
        values, or if they have inconsistent row sizes.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be
        multiplied.

    Returns:
        The product of the two matrices.
    """
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("invalid data type for einsum")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("invalid data type for einsum")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError
    ("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError
    ("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    try:
        result = np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("ma and mb can't be multiplied")

    return result
