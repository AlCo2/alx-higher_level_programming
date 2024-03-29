#!/usr/bin/python3
""" send json data using requests library """
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name,
                                                              repo_name)
    response = requests.get(url)
    i = 0
    for commit in response.json():
        if i == 10:
            break
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
        i += 1
