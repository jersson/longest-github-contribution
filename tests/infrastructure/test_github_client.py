from src.infrastructure.github_client import GitHubClient


# TODO: Improve this test case
def test_create_valid_class():
    user = "user-id"
    client = GitHubClient()

    assert client is not None


def test_valid_contribution():
    user = "jersson"
    client = GitHubClient()
    contributions = client.get_user_contributions(user)

    assert contributions is not None


def test_valid_longest_contribution():
    user = "jersson"
    client = GitHubClient()
    contributions = client.longest_contribution(user)

    assert contributions is not None
