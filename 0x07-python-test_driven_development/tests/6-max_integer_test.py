#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        #test with empty list, should return None
        self.assertIsNone(max_integer([]))
    def test_positive_ints(self):
        #test with positive integers, returns 4
        lst = [1, 2, 3, 4]
        self.assertEqual(max_integer(lst), 4)
    def test_negative_ints(self):
        #test with negative ints, return -1
        lst = [-1, -2, -3, -4]
        self.assertEqual(max_integer(lst), -1)
    def test_positive_negative(self):
        #test both positive and negative ints return 3
        lst = [-4, 1, 3, -2]
        self.assertEqual(max_integer(lst), 3)
    def test_one_int(self):
        #test one int, return int
        lst = [50]
        self.assertEqual(max_integer(lst), 50)
    def test_same_ints(self):
        #test same ints
        lst = [9, 9, 9, 9]
        self.assertEqual(max_integer(lst), 9)


if __name__ == '__main__':
    unittest.main()
