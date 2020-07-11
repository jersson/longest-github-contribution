from GitHubClient import GitHubClient


def test_create_valid_class():
    user = 'user-id'
    client = GitHubClient(user)

    assert client.user == user

def test_valid_contribution():
    user = 'jersson'
    client = GitHubClient(user)
    contributions = client.contributions()

    assert contributions is not None

def test_valid_longest_contribution():
    user = 'jersson'
    client = GitHubClient(user)
    contributions = client.longest_contribution()

    assert contributions is not None