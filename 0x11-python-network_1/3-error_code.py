#!/usr/bin/python3
"""Print http request error code"""
import urllib.request
import urllib.error
import sys


def error_msg():
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error Code: {e.code}")


if __name__ == "__main__":
    error_msg()
