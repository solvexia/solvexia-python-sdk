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
        response = api.apiGet(f"processruns/{self.processRunId}")
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
        response = api.apiGet(f"processruns/{self.processRunId}/runstatus")
        api.statusCodeCheck(response, "Error getting run status of a process run")
        return response.json()

    def getProcessRunDataSteps(self):
        response = api.apiGet(f"processruns/{self.processRunId}/steps")
        api.statusCodeCheck(response, "Error getting list of data steps")
        return response.json()
