#!/usr/bin/python3
"""
Unit tests for my_module.
"""

import unittest
from my_module import add, subtract


class TestMyModule(unittest.TestCase):
    """
    Test cases for my_module.
    """

    def test_add(self):
        """
        Test add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """
        Test subtract function.
        """
        self.assertEqual(subtract(4, 2), 2)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(-1, -1), 0)


if __name__ == '__main__':
    unittest.main()
