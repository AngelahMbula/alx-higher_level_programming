#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """represent Student."""
    def __init__(self, first_name, last_name, age):
        """method __init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
