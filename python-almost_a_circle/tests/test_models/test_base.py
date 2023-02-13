#!/usr/bin/python3
""" Doc """
import unittest
Base = __import__("base").Base

class test_Base(unittest.TestCase):
    """ Class test """

    def test_IdExist(self):
        """ unittest id exist """
        self.assertEqual(Base(), 1)

    def test_IdExist_plus1(self):
        """ unittest id exist """
        self.assertEqual(Base(), 2)

    def test_Id89(self):
        """ unittest id exist """
        self.assertEqual(Base(89), 89)
