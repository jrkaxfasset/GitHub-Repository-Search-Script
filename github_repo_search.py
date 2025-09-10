import requests

def search_github_repositories(query, top_n=5):
    """
    Searches GitHub repositories using the public API and prints the top results.

    :param query: Search query string.
    :param top_n: Number of top results to print.
    """
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_n
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message')}")
        return

    results = response.json().get('items', [])
    for idx, repo in enumerate(results, 1):
        print(f"{idx}. {repo['full_name']} - {repo['html_url']} (⭐ {repo['stargazers_count']})")

if __name__ == "__main__":
    query = input("Enter search query for GitHub repositories: ").strip()
    search_github_repositories(query)
