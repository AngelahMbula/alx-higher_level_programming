#!/usr/bin/python3
"""function class to JSON."""


def class_to_json(obj):
    """returns dictionary description for JSON serialization."""
    return obj.__dict__
