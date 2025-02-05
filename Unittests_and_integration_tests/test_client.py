#!/usr/bin/env python3

"""Test cases for client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class you test github org client"""

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/{google"),
        ("abc", "https://api.github.com/orgs/abc")
    ])
    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_org(self, org_name, expected_url, mock_org):
        self.client = GithubOrgClient(org_name)
        mock_org.return_value = {'repos_url': expected_url}

        result = self.client.org

        self.assertEqual(result, {'repos_url': expected_url})

    def test_public_repos_url(self):
        """Method used to test the method _public_repos_url"""
        mock_output = {'repos_url': 'https://mocked-url.com/orgs/repos'}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_output

            client = GithubOrgClient('test-org')

            result = client._public_repos_url

            self.assertEqual(result, 'https://mocked-url.com/orgs/repos')
