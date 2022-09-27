#!/usr/bin/python3
"""function that defines string to JSON."""


def to_json_string(my_obj):
    """returns the JSON representation of an object."""
    return json.dumps(my_obj)
