#!/usr/bin/python3
"""Script to fecth url status using requests module"""
import requests


url = "https://alx-intranet.hbtn.io/status"
resp = requests.get(url)
print(f"Body response:\n\t- type: {type(resp.text)}\n\t- content: {resp.text}")
