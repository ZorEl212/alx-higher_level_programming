#!/usr/bin/env python3
# A python script to get header of a http request

import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
        html = response.read()
        print(response.headers.get('X-Request-Id'))
