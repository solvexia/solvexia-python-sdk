#!/usr/bin/env python
import requests
import json
import sys


class solvexiaClient: 
    def __init__(self, env):
        self.env = env
        global baseUrl
        baseUrl = f"https://{env}.solvexia.com/api/v1/"

    def get_access_token(self, authFile):
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
        global accessToken 
        accessToken = self.authorisation

def status_code_check(response, errorMessage):
    if response.status_code != 200:
        print(errorMessage)
        print(response.json()['message'])
        sys.exit()

def api_post(urlPath, payload):
    headers = accessToken
    headers['Content-Type'] = 'application/json'
    response = requests.post(baseUrl + urlPath, data=json.dumps(payload), headers=headers)
    return response

def api_post_no_payload(urlPath):
    response = requests.post(baseUrl + urlPath, headers=accessToken)
    return response

def api_get(urlPath):
    response = requests.get(baseUrl + urlPath, headers=accessToken)
    return response