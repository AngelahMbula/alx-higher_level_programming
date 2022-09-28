#!/usr/bin/python3
"""function add_attribute."""


def add_attribute(obj, att, value):
    """adds new attribute to an object."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
