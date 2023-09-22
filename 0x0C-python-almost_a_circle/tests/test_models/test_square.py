#!/usr/bin/python3
"""
Test suite for Square class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareInstantiation(unittest.TestCase):
    """Test instantiation with various args"""

    def test_no_args(self):
        """Test instantiation with no args"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """
        args:
            size
        """
        s = Square(1)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_two_args(self):
        """
        args:
            size, x
        """
        s = Square(1, 2)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.x, 2)

    def test_three_args(self):
        """
        args:
            size, x, y
        """
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_four_args(self):
        """
        args:
            size, x, y, id
        """
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

class TestInvalidArgs(unittest.TestCase):
    """
    Test instantiation with invalid arguments
    Raises:
        TypeError if arg is not int
        ValueError if width and height are less than or equal to 0
                   if x and y are less than 0
    """
    def test_str_size(self):
        """
        args:
            size(str)
        """
        s = Square("1")
        self.assertRaises(TypeError)

    def test_size_zero(self):
        """
        args:
            size(0)
        """
        s = Square(0)
        self.assertRaises(ValueError)

    def test_neg_size(self):
        """
        args:
            size(-1)
        """
        s = Square(-1)
        self.assertRaises(ValueError)

    def test_str_x(self):
        """
        args:
            size, x(str)
        """
        s = Square(1, "2")
        self.assertRaises(TypeError)

    def test_neg_x(self):
        """
        args:
            size, x(-2)
        """
        s = Square(1, -2)
        self.assertRaises(ValueError)

    def test_str_y(self):
        """
        args:
            size, x, y(str)
        """
        s = Square(1, 2, "3")
        self.assertRaises(TypeError)

    def test_neg_y(self):
        """
        args:
            size, x, y(-3)
        """
        s = Square(1, 2, -3)
        self.assertRaises(ValueError)
