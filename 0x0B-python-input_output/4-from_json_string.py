#!/usr/bin/python3
"""convert from string to object"""

import json


def from_json_string(my_str):
    """return data structure represented by string"""
    return (json.loads(my_str))
