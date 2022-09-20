#!/usr/bin/python3
"""Defines square printing module"""


def print_square(size):
    """Prints square with #

    Args:
        size: height of square
    Raises:
        TypeError is size is not int
        ValueError if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
