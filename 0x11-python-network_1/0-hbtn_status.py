#!/usr/bin/python3
""" fetch data from a website using urllib"""
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print('- type: {}'.format(type(data)))
    print('- content: {}'.format(data))
    print('- utf8 content: {}'.format(data.decode('utf-8')))
