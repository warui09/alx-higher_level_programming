#!/usr/bin/python3
"""
Defines a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """
    Defines a class BaseGeometry (based on 5-base_geometry.py)

    Attributes:
        area(): raises an exception with the message
        'area() is not implemented'
        integer_validator(): validates an attribute value that is always
        a string
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
