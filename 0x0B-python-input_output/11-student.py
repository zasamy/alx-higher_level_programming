#!/usr/bin/python3
"""student class"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize last and first name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionnary representation"""
        if (type(attrs)) == list and all(type(a) == str for a in attrs):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of student"""
        for a in json:
            self.__dict__.update({a: json[a]})
