import unittest
from unittest.mock import Mock, patch

import pytest
from bs4 import BeautifulSoup

from src.infrastructure.html_parser import HtmlParser


class TestHtmlParser(unittest.TestCase):
    def test_validate_html_response_valid(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "text/html"}

        parser = HtmlParser()
        self.assertTrue(parser.validate_html_response(mock_response))

    def test_validate_html_response_invalid_status_code(self):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.headers = {"Content-Type": "text/html"}

        parser = HtmlParser()
        self.assertFalse(parser.validate_html_response(mock_response))

    @patch("requests.get")
    def test_parse_requested_url_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "text/html"}
        mock_response.content = b"<html><body>Content</body></html>"
        mock_get.return_value = mock_response

        parser = HtmlParser()
        result = parser.parse_requested_url("http://example.com")

        self.assertIsInstance(result, BeautifulSoup)
        self.assertEqual(result.text, "Content")

    # @pytest.mark.only
    @patch("requests.get")
    def test_parse_requested_url_invalid_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.headers = {"Content-Type": "text/html"}
        mock_get.return_value = mock_response

        parser = HtmlParser()
        result = parser.parse_requested_url("http://example.com")

        self.assertIsNone(result)
