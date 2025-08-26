#!/usr/local/bin/python
# coding=utf-8
"""
 Simple example of a Python script used to query an API.

 @note:    This is a simple example without any error handling.
 @license: http://data.gc.ca/eng/open-government-licence-canada
"""
import json
import requests

url      = 'http://www.earthquakescanada.nrcan.gc.ca/api/earthquakes/'
options  = { "Accept":"application/json", "Accept-Language":"en" }
response = requests.get(url, headers=options)
jdata    = response.json()

print jdata['metadata']['request']['name']['en']

for (key, value) in jdata['latest'].items():
    print key, "->", value