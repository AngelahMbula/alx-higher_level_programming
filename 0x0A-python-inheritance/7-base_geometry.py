#!/usr/bin/python3
"""function BaseGeometry."""


class BaseGeometry:
    """represent BaseGeometry class."""
    def area(self):
        """not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter as an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
