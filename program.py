from GitHubClient import GitHubClient
from utils import diff_in_days


def main():
    print("What's your GithHub account?")
    user = input()
    client = GitHubClient()

    print("Your longest contribution is...")
    longest_contributions = client.longest_contribution(user)

    lower_contribution_date = longest_contributions[0]
    higher_contribution_date = longest_contributions[1]
    contribution_days = diff_in_days(higher_contribution_date, lower_contribution_date)

    print("- start date {}".format(lower_contribution_date))
    print("- end date {}".format(higher_contribution_date))
    print("- {} days in a row!".format(contribution_days))


if __name__ == "__main__":
    main()
