#!/usr/bin/python3
""" script that get X-Rquest-id from the header """
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
