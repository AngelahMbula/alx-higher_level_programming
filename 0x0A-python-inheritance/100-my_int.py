#!/usr/bin/python3
"""function MyInt."""


class MyInt(int):
    """represents MyInt class."""
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
