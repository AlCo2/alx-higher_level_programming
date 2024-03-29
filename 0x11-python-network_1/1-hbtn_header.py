#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL"""
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
