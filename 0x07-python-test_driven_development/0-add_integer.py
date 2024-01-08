#!/usr/bin/python3
""" this is a unit test learning """


def add_integer(a, b=98):
    """function to add two integer """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
