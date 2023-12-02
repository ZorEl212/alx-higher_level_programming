#!/usr/bin/python3
"""Send POST request with email address using requests library"""
import requests
import sys


def send_email():
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    res = requests.post(url, params=values)
    print(res.text)


if __name__ == "__main__":
    send_email()
