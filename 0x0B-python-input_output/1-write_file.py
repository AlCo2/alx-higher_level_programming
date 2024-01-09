#!/usr/bin/python3
""" this is a function that write to a file
    and return the number of charactere writen
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
