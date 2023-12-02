#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request"""
import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]

values = {'email': email}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
