#!/usr/bin/python3
"""takes in a url, sends a request to the url and display value."""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
