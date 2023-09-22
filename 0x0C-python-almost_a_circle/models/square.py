#!/usr/bin/python3
"""
Defines a class Square that inherits from the Rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Defines a class Square that inherits from the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.
        
        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

     @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for the size attribute.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")
        self.width = size
        self.height = size

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the square.
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Setter for the x-coordinate attribute.

        Args:
            x (int): The x-coordinate of the square.

        Raises:
            ValueError: If x is not a non-negative integer.
        """
        if not isinstance(x, int) or x < 0:
            raise ValueError("x must be a non-negative integer")
        self._x = x

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the square.
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Setter for the y-coordinate attribute.

        Args:
            y (int): The y-coordinate of the square.

        Raises:
            ValueError: If y is not a non-negative integer.
        """
        if not isinstance(y, int) or y < 0:
            raise ValueError("y must be a non-negative integer")
        self._y = y
 @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for the size attribute.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must > 0")
        self.width = size
        self.height = size

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the square.
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Setter for the x-coordinate attribute.

        Args:
            x (int): The x-coordinate of the square.

        Raises:
            TypeError: If x is not an integer
            ValueError: If x is less than 0.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self._x = x

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the square.
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Setter for the y-coordinate attribute.

        Args:
            y (int): The y-coordinate of the square.

        Raises:
            TypeError: If y is not an integer
            ValueError: If y is less than 0.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self._y = y


    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: A string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
