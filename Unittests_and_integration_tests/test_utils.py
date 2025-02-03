#!/usr/bin/env python3

"""Unnittesting"""
from utils import access_nested_map
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """Class used for unit testing Utils.py """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """This is test that I'm returning what I'm suppose to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
