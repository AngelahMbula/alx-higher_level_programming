#!/usr/bin/python3
"""function Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents Square class."""

    def __init__(self, size):
        """initializes Square class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
