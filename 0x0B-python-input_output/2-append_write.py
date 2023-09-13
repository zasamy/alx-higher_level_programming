#!/usr/bin/python3
"""stringn to file"""


def append_write(filename="", text=""):
    """append string to file"""
    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
