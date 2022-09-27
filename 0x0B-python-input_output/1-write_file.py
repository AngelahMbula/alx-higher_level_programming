#!/usr/bin/python3
"""function that writes string into a text file."""


def write_file(filename="", text=""):
    """writes a string to a UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
