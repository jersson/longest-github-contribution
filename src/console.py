from src.infrastructure.github_client import GitHubClient
from src.infrastructure.html_parser import HtmlParser
from src.utils.date import diff_in_days


def main():
    print("What's your GitHub account?")
    user = input()

    print("Your longest contribution is...")
    parser = HtmlParser()
    client = GitHubClient(parser)
    longest_contributions = client.longest_contribution(user)

    start_contribution_date = longest_contributions[0]
    end_contribution_date = longest_contributions[1]
    contribution_in_days = diff_in_days(end_contribution_date, start_contribution_date)

    print("- start date {}".format(start_contribution_date))
    print("- end date {}".format(end_contribution_date))
    print("- {} days in a row!".format(contribution_in_days))


if __name__ == "__main__":
    main()
