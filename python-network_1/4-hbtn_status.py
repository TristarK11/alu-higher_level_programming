#!/usr/bin/python3
import requests

url = "http://0.0.0.0:5050/status"

# Fetching the URL using requests
response = requests.get(url)

# Displaying the response body
print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
