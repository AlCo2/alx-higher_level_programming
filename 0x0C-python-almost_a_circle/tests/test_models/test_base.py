#!/usr/bin/python3
""" unittest for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ class to test The base Clsas """

    def test_init(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id(self):
        base = Base(31)
        self.assertEqual(base.id, 31)


if __name__ == '__main__':
    unittest.main()
