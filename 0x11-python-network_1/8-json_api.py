#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if sys.argv[1]:
        query_param = {"q": sys.argv[1]}
    else:
        query_param = {"q": ""}

    res = requests.post(url, params=query_param)

    if res.text:
        try:
            data = res.json()
            if data:
                print("[{}] {}".format(data.get("id"), data.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("No result")
