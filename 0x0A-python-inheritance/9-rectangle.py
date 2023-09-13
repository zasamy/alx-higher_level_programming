#!/usr/bin/python3
"""geometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """initialize height and width"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implement area"""
        return (self.__height * self.__width)

    def __str__(self):
        """returns rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
