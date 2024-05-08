#!/usr/bin/python3
"""Function to Top ten the Query."""
import requests
from sys import argv

def number_of_subscribers(subreddit):
    """REturn Total 10 number on a given subreddit."""
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
