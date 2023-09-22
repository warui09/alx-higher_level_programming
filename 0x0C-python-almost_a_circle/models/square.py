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

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: A string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
