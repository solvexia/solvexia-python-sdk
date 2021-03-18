#!/usr/bin/env python

import requests
import json

def __init__(self, client_id, client_secret, env):
    self._client_id = client_id
    self._client_secret = client_secret

    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(f"https://{env}.solvexia.com/oauth/token", data=payload)
    if response.status_code != 200:
        print("Error with generating an Access Token via Client Credential Flow")
        sys.exit()
    self._access_token = response.json()["access_token"]
    self._authorisation = {'Authorization: 'Bearer ' + self._accesstoken}