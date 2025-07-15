#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the top 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """Prints the top 10 hot posts for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:topten:v1.0 (by /u/fakebot)'}

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data")
        if not data or "children" not in data:
            return None

        posts = data.get("children")
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        return None

