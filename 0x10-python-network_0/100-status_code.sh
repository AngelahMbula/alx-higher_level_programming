#!/bin/bash
# sends a request to url passed as an argument, displays the status code.
curl -sL -o /dev/null -w "%{http_code}" "$1"
