#!/usr/bin/env python3
"""
Unit test Test client
"""
import unittest
from unittest.mock import patch, PropertyMock

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class methods
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mocked):
        """ a method to test TestGithubOrgClient's org method """
        client = GithubOrgClient(org)
        test_response = client.org
        mocked.assert_called_once_with(
            "https://api.github.com/orgs/{org}".format(org=org))
        self.assertEqual(test_response, mocked.return_value)

    def test_public_repos_url(self):
        """ a method to test that the result of _public_repos_url is the
        expected one based on the mocked payload
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock,
                   return_value={"repos_url": "World"}) as mock:
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, "World")
