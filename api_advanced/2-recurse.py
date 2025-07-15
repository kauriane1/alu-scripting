#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively queries the Reddit API and returns a list of all hot article titles"""
    if hot_list is None:
        hot_list = []
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    if after:
        url += "?after={}".format(after)
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return None
    
    data = response.json().get("data")
    if data is None:
        return None
    
    children = data.get("children")
    if not children:
        return None if not hot_list else hot_list
    
    for child in children:
        hot_list.append(child.get("data").get("title"))
    
    after_token = data.get("after")
    if after_token:
        return recurse(subreddit, hot_list, after_token)
    
    return hot_list
