#!/usr/bin/python3
"""Defines a name printing module"""


def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name: first name to print
        last_name: last name to print
    Raises:
        TypeError: if either names are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
