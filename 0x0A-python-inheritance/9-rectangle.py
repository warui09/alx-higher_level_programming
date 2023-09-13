#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle that inherits from BaseGeometry
    Attributes:
        width, height: both are private members validated
        by integer_validator
    """

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
