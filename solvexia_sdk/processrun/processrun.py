#!/usr/bin/env python

import requests
import json
import sys

class processruns:
    def __init__(self, authorisation, processRunId);
        self.authorisation = authorisation
        self.processRunId = processRunId
        self.baseUrl = "https:///app.solvexia.com/api/v1/"

    def getProcessRun(self):
        getProcessRunUrl = self.baseUrl + f"processruns/{self.processRunId}"
        response = requests.get(getProcessRunUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting the specified process run")
            sys.exit()
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
        if response.status_code != 200:
            print("Error starting process run")
            sys.exit()
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
        if response.status_code() != 200:
            print("Error cancelling process run")
            sys.exit()
        return response.json()

    def processStatus(self):
        processStatusUrl = self.baseUrl + f"processruns/{self.processRunId}/runstatus"
        response = requests.get(processStatusUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting run status of a process run")
            sys.exit()
        return response.json()

    def processRunDataSteps(self):
        processDataStepsUrl = self.baseUrl + f"processruns/{self.processRunId}/steps"
        response = requests.get(processDataStepsUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error getting list of data steps")
            sys.exit()
        return response.json()
