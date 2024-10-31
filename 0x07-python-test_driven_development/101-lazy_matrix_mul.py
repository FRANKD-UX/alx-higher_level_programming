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

    Returns:
        The product of the two matrices.
    """
    return np.matmul(m_a, m_b)
