#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """creates a square."""

    def __init__(self, size=0):
        """define instance attribute."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """gives the area of suare"""
        return (self.__size ** 2)
