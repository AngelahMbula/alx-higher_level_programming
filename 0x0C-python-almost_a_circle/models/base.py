#!/usr/bin/python3
"""function Base class."""
import json
import csv
import turtle


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
