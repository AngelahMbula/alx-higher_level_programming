#!/usr/bin/python3
"""function that creates an object from JSON file."""
import json


def load_from_json_file(filename):
    """creates Object from JSONfile."""
    with open(filename) as f:
        return json.load(f)
