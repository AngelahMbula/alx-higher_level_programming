#!/usr/bin/python3
"""function that appends a strings."""


def append_write(filename="", text=""):
    """appends a string to UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
