#!/usr/bin/python3
"""
Defines a student by:
Public instance attributes:
first_name
last_name
age
Public method def to_json(self, attrs=None): that retrieves a
dictionary representation of a Student instance
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str, optional): List of attribute names to retrieve.
                If None, all attributes are retrieved.

        Returns:
            dict: A dictionary containing the attribute names and values.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
