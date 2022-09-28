#!/usr/bin/python3
"""function Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent Rectangle class."""

    def __init__(self, width, height):
        """initializes class."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """implements area."""
        return self.__width * self.__height

    def __str__(self):
        """prints."""
        return ("[Rectangle]" + str(self.__width) + "/" + str(self.__height))
