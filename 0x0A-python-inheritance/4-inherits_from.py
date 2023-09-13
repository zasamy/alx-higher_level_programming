#!/usr/bin/python3
"""sub class task"""


def inherits_from(obj, a_class):
    """True if inhirited object , false otherwise"""
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
