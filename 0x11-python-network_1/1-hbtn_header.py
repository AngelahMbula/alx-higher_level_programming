#!/usr/bin/python3
"""takes in url, sends a request to the url and displays value."""
import urllib.request


if __name__ == "__main__":
    import sys

    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(dict(resp.headers).get('X-Request-Id'))
