#!/usr/bin/env python3

"""Unnittesting"""
from utils import access_nested_map, get_json
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """Class used for unit testing access_nested_map()"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """This is test that I'm returning what I'm suppose to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """This is to test to make sure we are raising the right exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Class used for unittesting get_json()"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_get):
        """Method used to test to see if a json is returned"""
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        result = get_json(url)

        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)
