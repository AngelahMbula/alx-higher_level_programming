#!/usr/bin/python3
"""function Base class."""
import json
import csv


class Base:
    """Base of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
