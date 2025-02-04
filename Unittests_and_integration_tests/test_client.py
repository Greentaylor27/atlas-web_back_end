#!/usr/bin/env python3

"""Test cases for client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client



class TestGithubOrgClient(unittest.TestCase):
    """Class you test github org client"""

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/{google"),
        ("abc", "https://api.github.com/orgs/abc")
    ])
    @patch.object(client.GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_org(self, org_name, expected_url, mock_org):
        self.client = client.GithubOrgClient(org_name)
        mock_org.return_value = {'repos_url': expected_url}

        result = self.client.org

        self.assertEqual(result, {'repos_url': expected_url})
