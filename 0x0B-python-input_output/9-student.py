#!/usr/bin/python3
"""student class"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """initialize last and first name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionnary representation"""
        return (self.__dict__)
