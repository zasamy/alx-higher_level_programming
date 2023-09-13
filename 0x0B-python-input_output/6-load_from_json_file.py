#!/usr/bin/python3
"""object from json file"""

import json


def load_from_json_file(filename):
    """creates an obj from json file"""
    with open(filename, 'r', encoding="UTF8") as f:
        return (json.load(f))
