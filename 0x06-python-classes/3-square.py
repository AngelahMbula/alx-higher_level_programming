#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Initialize class square."""
    def __init__(self, size=0):
    """Initializing."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Return area of square."""
    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)
