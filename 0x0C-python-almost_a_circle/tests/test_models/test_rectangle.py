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

    def test_id(self):
        """Test if id is incremented or value passed"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width_string(self):
        """Test creation of Rectangle with width of string value"""
        r4 = Rectangle("2", 10)
        self.assertRaises(TypeError)

    def test_negative_height(self):
        """Test creation with negative height"""
        r5 = Rectangle(5, -10)
        self.assertRaises(ValueError)

    def test_negative_x(self):
        """Test creation with negative x"""
        r6 = Rectangle(4, 8, -9, 0)
        self.assertRaises(ValueError)

    def test_string_y(self):
        """Test creation with a string for value y"""
        r7 = Rectangle(4, 4, 0, "3", 9)
        self.assertRaises(TypeError)


if __name__ == "__main__":
    unittest.main()
