#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`."""
import requests
import sys


def search_user():
    """Sends a POST request to http://"""
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    res = requests.post(url, data=payload)
    try:
        json = res.json()
        if json:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
