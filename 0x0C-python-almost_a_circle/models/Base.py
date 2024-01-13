#!/usr/bin/python3
""" file that represant a base class"""


class Base:
    """
    base class that will be the base of all other
    classes in this projcet
    """

    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
