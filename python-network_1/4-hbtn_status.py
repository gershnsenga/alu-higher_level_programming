#!/usr/bin/python3
"""_summary_
- Write a Python script that
- fetches https://intranet.hbtn.io/status.
"""
import requests


if _name_ == "_main_":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format("OK" if len(r.text) > 100 else r.text))
