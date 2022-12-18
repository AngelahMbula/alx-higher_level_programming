#!/bin/bash
# takes in url and displays all http methods server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
