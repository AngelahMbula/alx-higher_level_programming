#!/usr/bin/python3
"""function that writes an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON rep."""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
