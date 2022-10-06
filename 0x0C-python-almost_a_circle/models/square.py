#!/usr/bin/python3
"""function Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits rom Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes class Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set size of Square class."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
