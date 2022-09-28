#!/usr/bin/python3
"""function Rectangle."""


class Rectangle(BaseGeometry):
    """represents a Rectangle class."""

    def __init__(self, width, height):
        """initialize a new rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
