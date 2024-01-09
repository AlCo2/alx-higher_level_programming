#!/usr/bin/python3
"""this is a function that read content of a file"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read())
