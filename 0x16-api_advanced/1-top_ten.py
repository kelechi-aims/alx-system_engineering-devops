#!/usr/bin/python3
''' Function that queries the Reddit API '''
import requests


def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    # Set a custom User-Agent header as Reddit requires it
    headers = {"User-Agent": "MyRedditBot"}

    response = requests.get(url, headers=headers)

    # Check if the subreddit exists and the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
            print("None")
