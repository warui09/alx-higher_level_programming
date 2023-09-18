#!/usr/bin/python3
"""
Test the area method in the Rectangle class

Returns the area of the rectangle
"""

import unittest
from models.rectangle import Rectangle


class testRectangleArea(unittest.TestCase):
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
