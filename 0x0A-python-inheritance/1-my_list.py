#!/usr/bin/python3
"""function my_list."""


class MyList(list):
    """implements sorted printing."""

    def print_sorted(self):
        """prints a list in sorted order."""
        print(sorted(self))
