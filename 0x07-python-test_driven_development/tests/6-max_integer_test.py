#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_max_at_end(self):
        """Test with the max integer at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with the max integer in the middle of the list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        """Test with a single negative number in the list."""
        self.assertEqual(max_integer([-1]), -1)

    def test_only_negative_numbers(self):
        """Test with a list of only negative numbers."""
        self.assertEqual(max_integer([-3, -2, -5, -7]), -2)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
