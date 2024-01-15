#!/usr/bin/python3
""" unittest for Rectangle """
import unittest
from models.rectangle import Rectangle

class testRectangle(unittest.TestCase):

    def testArea(self):
        r = Rectangle(11, 2)
        self.assertEqual(r.area(), 22)

    def testWithXandY(self):
        r = Rectangle(2, 4, 1, 5)
        self.assertEqual(r.area(), 8)

