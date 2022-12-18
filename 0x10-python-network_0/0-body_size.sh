#!/bin/bash
# takes in a url, sends a request and display the size
curl -s "$1" | wc -c
