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
        """
        Getter for the width property
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
        """
        Getter for the height property
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
        """
        Getter for x
        Returns the value of x
        """
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
        """
        Getter for y
        Returns the value of y
        """
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
        """
        Calculates the area of the rectangle
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints a representation of the rectangle using '#' and 'x' and 'y' offsets
        """
        for y_offset in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: A string representation of the Square.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """
        Assigns arguments to attributes in the specified order:
        1st argument: id attribute
        2nd argument: width attribute
        3rd argument: height attribute
        4th argument: x attribute
        5th argument: y attribute
        """
        if len(args) >= 1:
            self.__id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
