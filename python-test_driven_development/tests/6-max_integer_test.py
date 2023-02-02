#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_beginning(self):
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_middle(self):
        self.assertEqual(max_integer([3, 4, 2]), 4)
    
    def test_one_negatif_number(self):
        self.assertEqual(max_integer([-4, 3, 1, 2]), -4)
    
    def test_only_negatif_number(self):
        self.assertEqual(max_integer([-4, -3, 1, 2]), [-4, -3])

    def list_of_one_element(self):
        self.assertEqual(max_integer([2]), 2)

    def list_is_empty(self):
        self.assertEqual(max_integer([]), None)
