#!/usr/bin/env python3
"""
Unit test Test client
"""
import unittest
from unittest.mock import patch

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
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        mocked.assert_called_once_with(
            "https://api.github.com/orgs/{org}".format(org=org))
        self.assertEqual(test_response, mocked.return_value)
