#!/bin/bash
# use curl to detect how many word in response
curl -s "$1" | wc -c
