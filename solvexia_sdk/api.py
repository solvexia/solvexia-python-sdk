#!/usr/bin/env python
import requests
import json
import sys


class solvexia_client: 
    def __init__(self, env):
        self.env = env
        global baseUrl
        baseUrl = f"https://{env}.solvexia.com/api/v1/"

    def getAccessToken(self, authFile):
        with open(authFile) as jsonAuthFile:
            payload = json.load(jsonAuthFile)
        payload['grant_type'] = 'client_credentials'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"https://{self.env}.solvexia.com/oauth/token", data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Error generating an Access Token via Client Credential Flow")
            sys.exit()
        self.accessToken = response.json()['access_token']
        self.authorisation = {'Authorization': 'Bearer ' + self.accessToken}
        global access_token 
        access_token = self.authorisation

def statusCodeCheck(response, errorMessage):
    if response.status_code != 200:
        print(errorMessage)
        print(response.json()['message'])
        sys.exit()

def apiPost(urlPath, payload):
    headers = access_token
    headers['Content-Type'] = 'application/json'
    response = requests.post(baseUrl + urlPath, data=json.dumps(payload), headers=headers)
    return response

def apiPostNoPayload(urlPath):
    response = requests.post(baseUrl + urlPath, headers=access_token)
    return response

def apiGet(urlPath):
    response = requests.get(baseUrl + urlPath, headers=access_token)
    return response