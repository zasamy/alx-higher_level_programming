#!/usr/bin/python3

"""prints a square"""


def print_square(size):
    """prints a square with #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        print('#' * size)
