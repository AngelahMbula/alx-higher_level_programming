#!/bin/bash
# sends JSON POST request to url and displays body of reponse.
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
