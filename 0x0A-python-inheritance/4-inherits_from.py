#!/usr/bin/python3
"""function inherits."""


def inherits_from(obj, a_class):
    """returns true if object is an instance of class."""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
