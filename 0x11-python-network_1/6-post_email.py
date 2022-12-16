#!/usr/bin/python3
"""takes in a url and email, sends post request to the url."""
import sys
import requests


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=value)
    print(r.text)
