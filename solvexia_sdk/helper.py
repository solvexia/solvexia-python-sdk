#!/usr/bin/env python

import requests
import json
import sys

def statusCodeCheck(response, errorMessage):
    if response.status_code != 200:
        print(errorMessage)
        print(response.json().message)
        sys.exit()

"""def api_post(url, authorisation, payload):
    headers = authorisation
    headers['Content-Type'] = 'application/json'
    return response = requests.post(url, data=json.dumps(payload), headers=headers)}"""