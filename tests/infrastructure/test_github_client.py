import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import Mock

import pytest

from src.infrastructure.github_client import GitHubClient
from src.infrastructure.html_parser import HtmlParser


class TestGitHubClient(unittest.TestCase):
    def test_get_user_contributions_success(self):
        mock_parser = Mock(HtmlParser)
        mock_html = Mock()
        mock_element = {}
        mock_element["data-level"] = 1
        mock_element["data-date"] = "2024-01-01"

        mock_html.select.return_value = [mock_element]
        mock_parser.parse_requested_url.return_value = mock_html

        requested_url = "https://github.com/test_user"

        client = GitHubClient(mock_parser)
        data = client.get_user_contributions("test_user")

        self.assertEqual(data, [(datetime(2024, 1, 1), 1)])
        mock_parser.parse_requested_url.assert_called_once_with(requested_url)

    def test_get_user_contributions_invalid_data(self):
        mock_parser = Mock(HtmlParser)
        mock_html = Mock()
        mock_html.select.return_value = []
        mock_parser.parse_requested_url.return_value = mock_html

        client = GitHubClient(mock_parser)
        data = client.get_user_contributions("test_user")

        self.assertEqual(data, [])
