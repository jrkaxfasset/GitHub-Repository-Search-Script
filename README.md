# GitHub Repository Search Script

This Python script allows you to search for repositories on GitHub using the GitHub API and prints the top 5 results based on your query.

## Features

- Prompts for a search query.
- Fetches repositories from GitHub sorted by stars.
- Prints the top 5 repositories with their name, URL, and star count.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Usage

1. Save the script as `github_repo_search.py`.
2. Run the script:

   ```bash
   python github_repo_search.py
   ```

3. Enter your search query when prompted.

## Example

```
Enter search query for GitHub repositories: machine learning
1. scikit-learn/scikit-learn - https://github.com/scikit-learn/scikit-learn (⭐ 56000)
2. keras-team/keras - https://github.com/keras-team/keras (⭐ 60000)
...
```

## Notes

- The script uses the public GitHub API. For high-frequency searches, you may need to use a GitHub personal access token to avoid rate limiting.
