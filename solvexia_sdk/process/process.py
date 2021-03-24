#!/usr/bin/env python
import requests
import json
import sys
from solvexia_sdk import api

class process:
    def __init__(self, processId);
        self.processId = processId
        self.baseUrl = "https:///app.solvexia.com/api/v1/processes"
    
    def getProcessList(self):
        response = requests.get(self.baseUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting process list")
        return response.json()
    
    def getProcess(self):
        getProcessUrl = self.baseUrl + f'/{self.processId}'
        response = requests.get(getProcessUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting chosen process")
        return response.json()

    def createProcessRun(self):
        response = api.apiPostNoPayload(f"processes/{self.processId}/processruns")
        api.statusCodeCheck(response, "Error creating process run")
        return response.json()

    def getProcessRunList(self):
        processRunUrl = self.baseUrl + f"/{self.processID}/processruns"
        response = requests.get(processRunUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting run list")
        return response.json()
    
    def getProcessDataStepList(self):
        processDataStepUrl = self.baseUrl + f"/{self.processID}/steps"
        response = requests.get(processDataStepUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting data step list")
        return response.json()