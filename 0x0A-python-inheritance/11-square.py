#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle

    Attributes:
        size: must be an integer
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size**2

    def display(self):
        print("[Rectangle] {}/{}".format(self.__size, self.__size))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
