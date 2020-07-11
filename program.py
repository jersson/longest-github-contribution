from GitHubClient import GitHubClient


def get_contribution_list():
    print('What\'s your GithHub account?')
    user = input()
    client = GitHubClient(user)

    print('Your longest contribution is...')
    contributions = client.longest_contribution()
    start_longest_contribution = contributions[0]
    end_longest_contribution = contributions[1]
    
    print('- start date {} with {} contributions'.format(start_longest_contribution[1], start_longest_contribution[2]))
    print('- end date {} with {} contributions'.format(end_longest_contribution[1], end_longest_contribution[2]))
    print('- {} days in a row!'.format(end_longest_contribution[0] - start_longest_contribution[0] + 1))
get_contribution_list() 