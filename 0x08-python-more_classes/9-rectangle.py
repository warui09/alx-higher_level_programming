#!/usr/bin/python3
"""defines a rectangle by: (based on 8-rectangle.py)
   Class attributes:
   number_of_instances
        public attribute that tracks number of instances
   print_symbol
        initialized to '#'
        can be any type
   """


class Rectangle:
    """Attributes for the Rectangle module
    width
        private instance attribute that must be an
        integer greater than 0
    height
        private instance attribute that must be an
        integer greater than 0
    area()
        public method that returns the area
    perimeter()
        public method that returns the perimeter, if
        width or height is 0 return 0
    str()
        prints the rectangle with '#', if width or
        height is 0 print an empty string
    repr()
        return string representation of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                result += "".join(self.print_symbol) * self.__width
                if i != self.__height - 1:
                    result += "\n"
            return result

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
