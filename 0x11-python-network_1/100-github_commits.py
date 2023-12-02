#!/usr/bin/python3
"""Get the last 10 commit sha and Author from a repo"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url)
    for i in range(10):
        print(f"{res.json()[i]['sha']}: {res.json()[i]['commit']['author']['name']}")
