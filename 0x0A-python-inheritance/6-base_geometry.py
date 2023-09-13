#!/usr/bin/python3
"""
Defines a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """
    Defines a class BaseGeometry (based on 5-base_geometry.py)

    Attributes:
        area(): raises an exception with the message
        'area() is not implemented'
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
