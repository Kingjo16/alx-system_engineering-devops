#!/usr/bin/python3
"""Function to To the Query."""
import requests

def number_of_subscribers(subreddit):
    """Total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    respo = requests.get(url, headers=headers, allow_redirects=False)
    if respo.status_code == 200:
        data = respo.json()
        subs = data['data']['subscribers']
        return subs
    else:
        return 0
