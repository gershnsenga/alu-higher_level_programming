#!/usr/bin/python3
"""_summary_
- Write a Python script that
- fetches https://intranet.hbtn.io/status.
"""
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Error: Unable to fetch data from the URL. Status code:", response.status_code)

