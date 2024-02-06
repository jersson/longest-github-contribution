from HtmlParser import HtmlParser
from bs4 import BeautifulSoup
from datetime import datetime

from utils import diff_in_days, next_day


class GitHubClient:
    def __init__(self):
        pass

    def get_user_contributions(self, user: str) -> list:
        url = "https://github.com/{}".format(user)
        parser = HtmlParser()
        html: BeautifulSoup
        html = parser.request(url)

        if html is not None:
            contributions = html.select("[data-level][data-date]")
            data = []
            for element in contributions:
                try:
                    data_date = datetime.strptime(element["data-date"], "%Y-%m-%d")
                    data_level = element["data-level"]
                    data.append((data_date, data_level))
                except ValueError:
                    pass
            data.sort(key=lambda x: x[0])
            return data
        else:
            return []

    def longest_contribution(self, user: str) -> list:
        user_contributions = self.get_user_contributions(user)

        start_date = user_contributions[0][0]
        end_date = user_contributions[0][0]

        old_start_date = start_date
        old_end_date = end_date

        for contribution in user_contributions:
            if int(contribution[1]) > 0:
                end_date = contribution[0]
            else:
                current_diff_in_days = diff_in_days(end_date, start_date)
                old_diff_in_days = diff_in_days(old_end_date, old_start_date)
                if current_diff_in_days > old_diff_in_days:
                    old_end_date = end_date
                    old_start_date = start_date

                start_date = next_day(contribution[0])
                end_date = start_date

        current_diff_in_days = diff_in_days(end_date, start_date)
        old_diff_in_days = diff_in_days(old_end_date, old_start_date)

        if old_diff_in_days > current_diff_in_days:
            end_date = old_end_date
            start_date = old_start_date

        return [start_date, end_date]
