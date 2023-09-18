#!/usr/bin/python3
"""
Tests for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """
    Tests for Rectangle class
    """

    def test_create_r1(self):
        """Test if id is 1"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_create_r2(self):
        """Test if id is 2"""
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_create_r3(self):
        """Test if id is 12"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


if __name__ == "__main__":
    unittest.main()
