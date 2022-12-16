#!/usr/bin/python3
"""takes in url and email, sends a post request to the passed url."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')

    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
