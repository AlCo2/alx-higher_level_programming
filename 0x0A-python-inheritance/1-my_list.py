#!/usr/bin/python3
"""
    this is exemple of MyList that inherits from list
"""


class MyList(list):
    """ a class that ineherits another class """

    def print_sorted(self):
        temp = self[:]
        temp.sort()
        print(temp)
