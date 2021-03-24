#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class processruns:
    def __init__(self, processRunId);
        self.processRunId = processRunId
        self.baseUrl = "https:///app.solvexia.com/api/v1/"

    def getProcessRun(self):
        getProcessRunUrl = self.baseUrl + f"processruns/{self.processRunId}"
        response = requests.get(getProcessRunUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting the specified process run")
        return response.json()
    
    def startProcessRun(self):
        payload = {
            'request': 'ProcessRun_StartRq',
            'processRunId': self.processRunId
        }
        response = api.apiPost("requests", payload)
        api.statusCodeCheck(response, "Error starting process run")
        return response.json()

    def cancelProcessRun(self):
        payload = {
            'request': 'ProcessRun_CancelRq',
            'processRunId': self.processRunId
        }
        response = api.apiPost("requests", payload)
        api.statusCodeCheck(response, "Error cancelling process run")
        return response.json()

    def getProcessStatus(self):
        processStatusUrl = self.baseUrl + f"processruns/{self.processRunId}/runstatus"
        response = requests.get(processStatusUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting run status of a process run")
        return response.json()

    def getProcessRunDataSteps(self):
        processDataStepsUrl = self.baseUrl + f"processruns/{self.processRunId}/steps"
        response = requests.get(processDataStepsUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting list of data steps")
        return response.json()
