#!/usr/bin/python3
"""inhirited form task"""


def is_kind_of_class(obj, a_class):
    """checks if the object is instance or inhirited , or no"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
