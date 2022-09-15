#!/usr/bin/python3
"""defines a class square"""


class Square:
    """initialize class square"""
    def __init__(self, size=0):
    """initializing"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current area of square"""
        return (self.__size * self.__size)
