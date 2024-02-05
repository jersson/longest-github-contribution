from HtmlParser import HtmlParser
from bs4 import BeautifulSoup, Tag
from datetime import datetime, timedelta

from utils import log_error, diff_in_days, next_day


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

        lower_date = user_contributions[0][0]
        higher_date = user_contributions[0][0]

        old_lower_date = lower_date
        old_higher_date = higher_date

        for contribution in user_contributions:
            if int(contribution[1]) > 0:
                higher_date = contribution[0]
            else:
                current_diff_in_days = diff_in_days(higher_date, lower_date)
                old_diff_in_days = diff_in_days(old_higher_date, old_lower_date)
                if current_diff_in_days > old_diff_in_days:
                    old_higher_date = higher_date
                    old_lower_date = lower_date

                lower_date = next_day(contribution[0])
                higher_date = lower_date

        current_diff_in_days = diff_in_days(higher_date, lower_date)
        old_diff_in_days = diff_in_days(old_higher_date, old_lower_date)

        if old_diff_in_days > current_diff_in_days:
            higher_date = old_higher_date
            lower_date = old_lower_date

        return [lower_date, higher_date]
