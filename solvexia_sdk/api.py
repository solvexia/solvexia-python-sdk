#!/usr/bin/env python

import requests
import json
import sys
from helper import statusCodeCheck

class solvexia_client: 
    def __init__(self, clientId, clientSecret, env):
        self.clientIdd = clientId
        self.clientSecret = clientSecret
        self.env = env

    def acquireAccessToken(self):
        payload = {
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(f"https://{self.env}.solvexia.com/oauth/token", data=payload)
        statusCodeCheck(response.status_code, "Error with generating an Access Token via Client Credential Flow")
        self.accessToken = response.json()['access_token']
        self.authorisation = {'Authorization': 'Bearer ' + self._accesstoken}
        
        return self.authorisation