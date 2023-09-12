#!/usr/bin/python3
"""
Defines a student by: (based on 10-student.py)
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """Defines the student"""

    def __init__(self, first_name, last_name, age):
        """Instantiate the Student class"""

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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json: json data with Student attributes
        """

        for key, value in json.items():
            setattr(self, key, value)
