#!/usr/bin/python3
"""defines a square based on 2-square.py"""


class Square:
    """instantiate a square with optional sides
    size must be an integer greater than 0
    and an area method that returns the area of
    of the square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
