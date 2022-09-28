#!/usr/bin/python3
"""function is same class."""


def is_same_class(obj, a_class):
    """returns true if object is same as instance of specified class."""
    if type(obj) == a_class:
        return True
    return False
