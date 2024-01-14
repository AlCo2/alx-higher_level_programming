#!/usr/bin/python3
""" file that represant a base class"""


class Base:
    """
    base class that will be the base of all other
    classes in this projcet
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

