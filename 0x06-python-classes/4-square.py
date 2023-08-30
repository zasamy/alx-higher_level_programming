#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """creates squarre."""

    def __init__(self, size=0):
        """present an instance attribute."""
        self.size = size

    @property
    def size(self):
        """retrieve size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """gives area"""
        return (self.__size ** 2)
