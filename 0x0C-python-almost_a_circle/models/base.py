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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string representation of list dict"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """write json representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionnary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return the json list represnetation"""
        if json_string is None or json_string == "[]":
            return []
        return json.load(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return instances with all attributes"""
        if dictionary != {}:
            if cls.__name__ is 'Rectangle':
                a = cls(1, 1)
            if cls.__name__ is 'Square':
                a = cls(1)
            a.update(**dictionary)
            return (a)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dt) for dt in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        if cls.__name__ is "Rectangle":
            names = ['width', 'height', 'x', 'y', 'id']
        else:
            names = ['size', 'x', 'y', 'id']
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline='') as f:
            if list_objs:
                writer = csv.DictWriter(f, fieldnames=names)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())
            else:
                writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """desrialize in csv"""
        new = []
        filename = '{}.csv'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for i, j in row.items():
                        row[i] = int(j)
                    new.append(row)
            return([cls.create(**x) for x in new])
        except FileNotFoundError:
            return ([[]])
