#!/usr/bin/python3
""" send json data using requests library """
import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
