#!/usr/bin/python3
""" Doc """
import unittest
Base = __import__("base").Base

class test_Base(unittest.TestCase):
    """ Class test """

    def test_IdExist(self):
        """ unittest id exist """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_IdExist_plus1(self):
        """ unittest id exist """
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_Id89(self):
        """ unittest id exist """
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

if __name__ == '__main__':
    unittest.main()