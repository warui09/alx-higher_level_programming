#!/usr/bin/python3
"""0. Integers addition module

"""


def add_integer(a, b=98):
    """Return an integer, the result of adding two integers a, and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    return (int(a) + int(b))

