#!/usr/bin/python3
"""defines a square based on 3-square.py"""


class Square:
    """instantiate the square with optinal side that
    has to be an integer and greater than 0 and a
    getter and a setter method"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
