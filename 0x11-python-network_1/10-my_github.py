#!/usr/bin/python3
"""get github id using requests module"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    res = requests.get(url, auth=(user, passwd))
    print(res.json().get('id'))
