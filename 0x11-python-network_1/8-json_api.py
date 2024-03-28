#!/usr/bin/python3
""" send json data """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    q = sys.argv[2]
    response = requests.post(url, data={'q': q})
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
