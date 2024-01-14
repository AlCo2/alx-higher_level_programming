#!/usr/bin/python3
""" unittest for Rectangle """
import unittest
from models.rectangle import Rectangle

class testRectangle(unittest.TestCase):

    def testArea(self):
        r = Rectangle(11, 2)
        self.assertEqual(r.area(), 22)
