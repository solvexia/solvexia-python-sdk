#!/usr/bin/env python
import requests
import json
import sys

access_token = {}
baseUrl = f"https:///{env}.solvexia.com/api/v1/"

class solvexia_client: 
    def __init__(self, clientId, clientSecret, env):
        self.clientIdd = clientId
        self.clientSecret = clientSecret
        self.env = env

    def getAccessToken(self):
        payload = {
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(f"https://{self.env}.solvexia.com/oauth/token", data=payload)
        if response.status_code != 200:
            print("Error generating an Access Token via Client Credential Flow")
            sys.exit()
        self.accessToken = response.json()['access_token']
        self.authorisation = {'Authorization': 'Bearer ' + self.accesstoken}
        
        global access_token = self.authorisation

def statusCodeCheck(response, errorMessage):
if response.status_code != 200:
    print(errorMessage)
    print(response.json().message)
    sys.exit()

def apiPost(urlPath, payload):
    headers = access_token
    headers['Content-Type'] = 'application/json'
    return response = requests.post(baseUrl + urlPath, data=json.dumps(payload), headers=headers)}

def apiPostNoPayload(urlPath):
    return response = requests.post(baseUrl + urlPath, headers=access_token)