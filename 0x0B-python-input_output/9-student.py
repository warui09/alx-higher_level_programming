#!/usr/bin/python3
"""
Defines a student by:
    Public instances
    first_name
    last_name
    age
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
