#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import helper

class processruns:
    def __init__(self, authorisation, processRunId);
        self.authorisation = authorisation
        self.processRunId = processRunId
        self.baseUrl = "https:///app.solvexia.com/api/v1/"

    def getProcessRun(self):
        getProcessRunUrl = self.baseUrl + f"processruns/{self.processRunId}"
        response = requests.get(getProcessRunUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting the specified process run")
        return response.json()
    
    def startProcessRun(self):
        startProcessRunUrl = self.baseUrl + "requests"
        payload = {
            'request': 'ProcessRun_StartRq',
            'processRunId': self.processRunId
        }
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(startProcessRunUrl, data=json.dumps(payload), headers=headers)
        helper.statusCodeCheck(response, "Error starting process run")
        return response.json()

    def cancelProcessRun(self):
        cancelProcessRunUrl = self.baseUrl + "requests"
        payload = {
            'request': 'ProcessRun_CancelRq',
            'processRunId': self.processRunId
        }
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(cancelProcessRunUrl, data=json.dumps(payload), headers=headers)
        helper.statusCodeCheck(response, "Error cancelling process run")
        return response.json()

    def processStatus(self):
        processStatusUrl = self.baseUrl + f"processruns/{self.processRunId}/runstatus"
        response = requests.get(processStatusUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting run status of a process run")
        return response.json()

    def processRunDataSteps(self):
        processDataStepsUrl = self.baseUrl + f"processruns/{self.processRunId}/steps"
        response = requests.get(processDataStepsUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting list of data steps")
        return response.json()
