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

    @patch('client.get_json', return_value=[{"name": "Google"},
                                            {"name": "Twitter"}])
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value="hello world") as mock_public:
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            self.assertEqual(result, [item["name"] for item in json_payload])
            mock_public.assert_called_once()
        mock_json.assert_called_once()
