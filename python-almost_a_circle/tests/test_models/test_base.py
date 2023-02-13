#!/usr/bin/python3
""" Doc """
import unittest
Base = __import__('base').Base

class TestBase(unittest.TestCase):
    """ Class test """

    def testIdExist(self):
        """ unittest id exist """
        self.assertEqual(Base(), 1)

    def testIdExist_plus1(self):
        """ unittest id exist """
        self.assertEqual(Base(), 2)

    def testId89(self):
        """ unittest id exist """
        self.assertEqual(Base(89), 89)
