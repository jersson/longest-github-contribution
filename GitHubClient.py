from HtmlParser import HtmlParser
from utils import log_error
from bs4 import BeautifulSoup
from bs4 import Tag


class GitHubClient():
    def __init__(self, user: str):
        self.user = user
    
    def __has_data_date(self, tag: Tag):
        return tag.has_attr('data-date')

    def contributions(self) -> list:
        result = None
        try:
            url = 'https://github.com/{}'.format(self.user)
            parser = HtmlParser()
            html: BeautifulSoup
            html = parser.request(url)

            if html is not None:
                contributions =  html.findAll(self.__has_data_date)
                result =  contributions
        except Exception as error:
            log_error(error)
        finally:
            return result
