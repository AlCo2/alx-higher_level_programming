#!/usr/bin/python3
"""file for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class that inherit from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
