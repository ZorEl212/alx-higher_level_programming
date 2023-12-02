#!/usr/bin/python3
"""Get X-Request-Id of http request (using requests)"""
import requests
import sys


def get_xId():
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers['X-Request-Id'])


if __name__ == "__main__":
    get_xId()
