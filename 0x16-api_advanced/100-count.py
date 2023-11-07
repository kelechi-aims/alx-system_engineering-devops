#!/usr/bin/python3
''' Aecursive function that queries the Reddit API'''
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    '''
    parses the title of all hot articles, and prints a sorted
    count of given keywords (case-insensitive, delimited by spaces.
    '''
    if word_count is None:
        word_count = {}

    headers = {"User-Agent": "MyRedditBot"}

    params = {'after': after}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title.split():
                word_count[word] = word_count.get(word, 0) + 1

    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
