#! /usr/bin/python

import requests, json, os

if os.path.exists("/storage/debug"):
    url = "http://127.0.0.1:8000/portal/api/1.0/ansible/gen/inventory"
else:
    url = "http://127.0.0.1/portal/api/1.0/ansible/gen/inventory"
payload = {}
r = requests.post(url, data=payload)
print json.loads(r.content)['data']
