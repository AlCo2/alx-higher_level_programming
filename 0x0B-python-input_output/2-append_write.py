#!/usr/bin/python3
"""
    append to a file task
"""


def append_write(filename="", text=""):
    """
        a function that appends a string at
        the end of a text file (UTF8)
        and returns the number of characters added:
    """

    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
