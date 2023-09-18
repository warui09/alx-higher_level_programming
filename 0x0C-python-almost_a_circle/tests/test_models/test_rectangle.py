#!/usr/bin/python3
"""
Tests for Rectangle class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """
    Tests for Rectangle class
    """

    def test_id(self):
        """Test if id is incremented or value passed"""
        pass

    def test_no_args(self):
         with self.assertRaises(TypeError):
            Rectangle()

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

class TestRectangleArea(unittest.TestCase):
    """
    Test the area method in the Rectangle class
    """

    def test_rectangle_area(self):
        """Create instances of Rectangle and calculate their areas"""
        # create rectangles
        r1 = Rectangle(5, 10)
        r2 = Rectangle(8, 7, 0, 0, 12)

        # test area
        self.assertEqual(r1.area(), 50)
        self.assertEqual(r2.area(), 56)

if __name__ == "__main__":
    unittest.main()
