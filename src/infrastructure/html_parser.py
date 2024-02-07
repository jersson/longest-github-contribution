from contextlib import closing

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from src.utils.logs import log_error


class HtmlParser:
    def validate_html_response(self, res: requests.Response) -> bool:
        content_type = res.headers["Content-Type"].lower()

        return (
            res.status_code == 200
            and content_type is not None
            and content_type.find("html") > -1
        )

    def parse_requested_url(self, url: str) -> BeautifulSoup:
        response = None
        try:
            with closing(requests.get(url, stream=True)) as raw_response:
                if self.validate_html_response(raw_response):
                    response = BeautifulSoup(raw_response.content, "html.parser")

        except RequestException as error:
            log_error("Error making web requests to {}: {}".format(url, error))

        return response
