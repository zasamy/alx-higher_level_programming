#!/usr/bin/python3
"""base module"""


import json
import csv


class Base:
    """present base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
