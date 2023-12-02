#!/usr/bin/python3
import requests
import sys


repo = sys.argv[1]
owner = sys.argv[2]

url = f"https://api.github.com/repos/{owner}/{repo}/commits"

res = requests.get(url)
for i in range(10):
    print(f"{res.json()[i]['sha']}: {res.json()[i]['commit']['author']['name']}")
