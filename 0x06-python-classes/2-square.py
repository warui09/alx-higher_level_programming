#!/usr/bin/python3
"""defines a square based on 1-square.py"""


class Square:
    """instantiate a square with optional value size that is
    an integer greater than 0"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
