#!/usr/bin/python3
"""provides a function that queries the Reddit API and 
returns the number of subscribers"""
import json
from urllib.request import Request, urlopen
import uuid


def number_of_subscribers(subreddit):
    """returns number of reddit subbredit subscribers"""
    req = Request(f'https://www.reddit.com/r/{subreddit}/about.json')
    id = str(uuid.uuid4())
    req.add_header('User-Agent', f'api_advanced_client/python3 (/u/chol-{id}')
    res = urlopen(req)
    jdata = json.load(res)
    return jdata.get('data', {}).get('subscribers', 0)

