#!/usr/bin/python3
"""file for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class that inherit from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        return size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        set size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        update method
        """
        if len(args) < 1:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

    def to_dictionary(self):
        """
        to dict method
        """
        return {'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y}
