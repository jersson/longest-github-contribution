from HtmlParser import HtmlParser
from bs4 import BeautifulSoup, Tag
from datetime import datetime, timedelta

from utils import log_error, date_diff_in_days


class GitHubClient:
    def __init__(self, user: str):
        self.user = user

    def get_user_contributions(self) -> list:
        url = "https://github.com/{}".format(self.user)
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

    def longest_contribution(self) -> list:
        user_contributions = self.get_user_contributions()

        lower_date = user_contributions[0][0]
        higher_date = user_contributions[0][0]

        old_lower_date = lower_date
        old_higher_date = higher_date

        for contribution in user_contributions:
            if int(contribution[1]) > 0:
                higher_date = contribution[0]
            else:
                current_date_diff_in_days = date_diff_in_days(higher_date, lower_date)
                old_date_diff_in_days = date_diff_in_days(
                    old_higher_date, old_lower_date
                )
                if current_date_diff_in_days > old_date_diff_in_days:
                    old_higher_date = higher_date
                    old_lower_date = lower_date
                one_day = timedelta(days=1)
                lower_date = contribution[0] + one_day
                higher_date = lower_date

        current_date_diff_in_days = date_diff_in_days(higher_date, lower_date)
        old_date_diff_in_days = date_diff_in_days(old_higher_date, old_lower_date)

        if old_date_diff_in_days > current_date_diff_in_days:
            higher_date = old_higher_date
            lower_date = old_lower_date

        return [lower_date, higher_date]
