#!/usr/bin/env python
import requests
import json
import sys

class process:
    def __init__(self, authorisation, processId);
        self.authorisation = authorisation
        self.processId = processId
        self.baseUrl = "https:///app.solvexia.com/api/v1/processes"
    
    def processList(self):
        response = requests.get(self.baseUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting process list")
            sys.exit()
        return response.json()
    
    def getProcess(self):
        getProcessUrl = self.baseUrl + f'/{self.processId}'
        response = requests.get(getProcessUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting chosen process")
            sys.exit()
        return response.json()

    def createProcessRun(self):
        createProcessRunUrl = self.baseUrl + f"/{self.processID}/processruns"
        response = requests.post(createProcessRunUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error creating process run")
            sys.exit()
        return response.json()

    def processRunList(self):
        processRunUrl = self.baseUrl + f"/{self.processID}/processruns"
        response = requests.get(processRunUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting process run list")
            sys.exit()
        return response.json()
    
    def processDataStepList(self):
        processDataStepUrl = self.baseUrl + f"/{self.processID}/steps"
        response = requests.get(processDataStepUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting data step list")
            sys.exit()
        return response.json()