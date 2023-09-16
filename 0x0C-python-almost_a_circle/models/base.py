#!/usr/bin/python3
"""
Defines a class Base
"""


class Base:
    """
    Defines a class Base

    Attributes:
    __nb_objects: tracks instances othe Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the class with the provided id
        if no id is passed None is used
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
