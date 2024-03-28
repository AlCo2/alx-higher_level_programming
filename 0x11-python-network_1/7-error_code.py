#!/usr/bin/python3
""" get the code of a request """
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if (response.status_code >= 400):
        print('Error code:', response.status_code)
    else:
        print(response.text)
