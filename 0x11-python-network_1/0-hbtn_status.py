#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status."""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body Response:")
        print("\t- type {}".format(type(body)))
        print("\t- content {}".format(body))
        print("\t- utf-8 content {}".format(body.decode('utf-8')))
