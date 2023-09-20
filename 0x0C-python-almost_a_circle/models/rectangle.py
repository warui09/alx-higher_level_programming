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

        Args:
            width, height, x, y: integers
            id: integer or None
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for the width property
        Returns the width of the Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width property"""
        if width is None or not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for the height property
        Returns the height of the Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height property"""
        if height is None or not isinstance(width, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter for x
        Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for y
        Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a represntation of the rectangle using '#'"""
        for row in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Returns a string description of the Rectangle instance Attributes"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
