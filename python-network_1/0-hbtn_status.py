#!/usr/bin/python3
import urllib.request

url = "https://alu-intranet.hbtn.io/status"

# Fetching the URL with urllib
with urllib.request.urlopen(url) as response:
    body = response.read()

# Displaying the response body
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
