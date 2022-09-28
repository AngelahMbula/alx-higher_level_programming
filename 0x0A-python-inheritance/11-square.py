#!/usr/bin/python3
"""function Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents Square class."""

    def __init__(self, size):
        """initializes class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implements area."""
        return self.__size * self.__size

    def __str__(self):
        """prints"""
        return ("[Square]" + str(self.__size) + "/" + str(self.__size))
