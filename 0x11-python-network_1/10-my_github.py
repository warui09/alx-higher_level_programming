#!/usr/bin/python3
"""Takes GitHub credentials (username and password) and uses
the GitHub API to display id"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(user, passwd))

    if res.status_code == 200:
        print(res.json().get("id"))
