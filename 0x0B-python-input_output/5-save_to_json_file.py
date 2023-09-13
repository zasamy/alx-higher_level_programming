#!/usr/bin/python3
"""object to text file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file with json"""
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
