from GitHubClient import GitHubClient


def test_create_valid_class():
    user = 'user-id'
    client = GitHubClient(user)

    assert client.user == user

def test_get_valid_contribution_list():
    user = 'jersson'
    client = GitHubClient(user)
    contributions = client.contributions()

    assert contributions is not None