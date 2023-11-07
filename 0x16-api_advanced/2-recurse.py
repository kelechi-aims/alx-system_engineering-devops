#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""
import requests
import sys


def append_title(hot_list, posts):
    """ Appends item into a list """
    if len(posts) == 0:
        return
    hot_list.append(posts[0]["data"]["title"])
    posts.pop(0)
    append_title(hot_list, posts)


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot
    articles for a given subreddit
    """
    headers = {"User-Agent": "MyRedditBot"}

    params = {"after": after}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    dic = response.json()
    posts = dic["data"]["children"]
    append_title(hot_list, posts)
    after = dic["data"]["after"]
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
