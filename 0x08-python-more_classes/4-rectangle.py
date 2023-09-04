#!/usr/bin/python3

"""class for rectangle"""


class Rectangle:
    """class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize hight and width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """prints the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            S = ""
            for a in range(self.__height):
                for b in range(self.__width):
                    S += "#"
                if a < self.__height - 1:
                    S += "\n"
            return (S)

    def __repr__(self):
        """returns a rectangle representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
