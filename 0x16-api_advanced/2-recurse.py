#!/usr/bin/python3
''' Recursive function that queries the Reddit API '''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''
    Returns a list containing the titles of all hot articles
    for a given subreddit
    '''
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent header as Reddit requires it
    headers = {"User-Agent": "MyRedditBot"}
    response = requests.get(url, headers=headers)

    # Check if the subreddit exists and the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        # Extract titles and add them to the hot_list
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        # Check if there are more posts (pagination)
        after = data["data"]["after"]
        if after:
            recurse(subreddit, hot_list, after)
        else:
            # No more posts, return the hot_list
            return hot_list
    else:
        return None  # Return None for invalid subreddits or failed requests
