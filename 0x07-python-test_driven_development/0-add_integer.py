#!/usr/bin/python3
"""Defines an integer addition module"""


def add_integer(a ,b):
    """Returns the addition of a and b

    Raises:
        TypeError if either a or b is a noninteger or not a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
