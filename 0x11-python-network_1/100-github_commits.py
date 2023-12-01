#!/usr/bin/python3
"""Lists the last 10 commits by a user in a specified repository"""

import requests
import sys

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    res = requests.get(url)
    res = res.json()
    res = res[:10]
    for i in res:
        print("{}: {}".format(i["sha"], i["commit"]["author"]["name"]))
