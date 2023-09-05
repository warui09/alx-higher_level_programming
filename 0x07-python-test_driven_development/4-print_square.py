#!/usr/bin/python3
"""prints a square with the character #"""
def print_square(size):
    """Attributes
    size
        must be an integer, otherwise raise a TypeError
        with the message "size must be an integer"

        must be greater than 0, otherwise raise a ValueError
        with the message "size must be >= 0"

        if size is a float and is less than 0, raise a
        TypeError exception with the message "size must be an integer"
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print()

    for i in range(size):
        print("#" * size)
