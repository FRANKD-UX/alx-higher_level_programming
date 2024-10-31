#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-1, 3, -5, 10, 7]), 10)

    def test_single_element(self):
        """Test with a single-element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats_in_list(self):
        """Test with floats in the list."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5, 2.9]), 2.9)

    def test_all_identical_elements(self):
        """Test with all identical elements in the list."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_none_as_input(self):
        """Test if None is passed as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integer_in_list(self):
        """Test with non-integer types in the list."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
