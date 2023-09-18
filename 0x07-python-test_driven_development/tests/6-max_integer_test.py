#!/usr/bin/python3
"""Module for unittest on max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_cases(unittest.TestCase):
    """Test cases for the function"""
    def test_negative_numbers(self):
        """Test max value for negative numbers"""
        self.assertEqual(max_integer([-1, -4, -3, -10, -20, -100]), -1)
        self.assertEqual(max_integer([-2.44, -2.45, -100, -23, -2.43]), -2.43)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)
        self.assertEqual(max_integer([-1]), -1)

    def test_posative_numbers(self):
        """Test max value of posative numbers"""
        self.assertEqual(max_integer([1, 0, 100, 1000, 1000.2]), 1000.2)
        self.assertEqual(max_integer([0xffffffff, 4294967295, 1]), 4294967295)
        self.assertEqual(max_integer([0xffffffff, 4294967295, 1]), 0xffffffff)
        result = max_integer([0xffffffff, 4294967295.5, 1])
        self.assertEqual(result, 4294967295.5)

    def test_edge_cases(self):
        """Test for edge cases.
            with numbers that are huge"""
        result = max_integer([0, 0.1, -0.1, 0xffffffffffffffff])
        self.assertEqual(result, 0xffffffffffffffff)
        result = max_integer([float('inf'), 0xffffffffffffffff])
        self.assertEqual(result, float('inf'))
        self.assertNotEqual(result, 0xffffffffffffffff)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
