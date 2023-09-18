#!/usr/bin/python3
"""
Defines a class that inherits from the Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle class that inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter for the width property
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter for width property
        """
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be greater than 0")

    @property
    def height(self):
        """
        getter for the height property
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter for height property
        """
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be greater than 0")
