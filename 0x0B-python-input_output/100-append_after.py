#!/usr/bin/python3
"""function append_after."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file."""
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as m:
        m.write(text)
