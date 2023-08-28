#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except Exception as er:
        print("Exception:", er, file-sys.stderr)
        is_int = False
    return is_int
