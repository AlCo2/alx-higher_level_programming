#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.Request(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPerror as e:
        print(e.code())
