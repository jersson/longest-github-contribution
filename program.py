from GitHubClient import GitHubClient


def test_get_valid_contribution_list():
    print('What\'s your GithHub account?')
    user = input()
    client = GitHubClient(user)
    contributions = client.contributions()
    print('This is your contribution list...')
    for contribution in contributions:
        print('{} contributions on {}'.format(contribution['data-count'], contribution['data-date']))


test_get_valid_contribution_list()