#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, 'r', encoding="UTF8") as f:
        txtfile = f.read()
        print(txtfile, end="")
