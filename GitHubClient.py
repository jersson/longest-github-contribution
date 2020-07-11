from HtmlParser import HtmlParser
from utils import log_error
from bs4 import BeautifulSoup
from bs4 import Tag


class GitHubClient():
    def __init__(self, user: str):
        self.user = user
        self.__contributions = None
    
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
                self.__contributions
                result =  contributions
        except Exception as error:
            log_error(error)
        finally:
            return result
    
    def longest_contribution(self) -> list:
        result = []

        if self.__contributions is None:
            self.__contributions = self.contributions()

        max, min = 0, 0
        old_max, old_min = max, min
        for index in range(len(self.__contributions)):
            if int(self.__contributions[index]['data-count']) > 0:
                max = index
            else:
                if max - min > old_max - old_min:
                    old_max, old_min = max, min
                min = index + 1
                max = min
            
        if old_max - old_min > max - min:
            max, min = old_max, old_min

        for i in [min, max]:
            result.append([i, self.__contributions[i]['data-date'], self.__contributions[i]['data-count']])
        
        return result
