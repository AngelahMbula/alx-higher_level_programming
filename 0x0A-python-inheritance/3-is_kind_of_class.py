#!/usr/bin/python3
"""function is kind of class."""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class."""
    if isinstance(obj, a_class):
        return True
    return False
