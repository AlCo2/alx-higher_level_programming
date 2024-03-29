#!/usr/bin/python3
""" send json data using requests library """
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get("https://api.github.com/users/{}".format(username),
                            headers={
                                "Authorization": "Bearer {}".format(password),
                                "Accept": "application/vnd.github+json",
                                })
    user_id = response.json().get("id")
    print(user_id)
