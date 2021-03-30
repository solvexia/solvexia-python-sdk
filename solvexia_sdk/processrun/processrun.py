#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class processruns:
    def __init__(self, processRunId):
        self.processRunId = processRunId

    def getProcessRun(self):
        response = api.apiGet(f"processruns/{self.processRunId}")
        api.statusCodeCheck(response, f"Error getting the specified process run with processRunId {self.processRunId}")
        return response.json()
    
    def startProcessRun(self):
        payload = {
            'request': 'ProcessRun_StartRq',
            'processRunId': self.processRunId
        }
        response = api.apiPost("requests", payload)
        api.statusCodeCheck(response, f"Error starting process run with processRunId {self.processRunId}")
        return response.json()

    def cancelProcessRun(self):
        payload = {
            'request': 'ProcessRun_CancelRq',
            'processRunId': self.processRunId
        }
        response = api.apiPost("requests", payload)
        api.statusCodeCheck(response, f"Error cancelling process run with processRunId {self.processRunId}")
        return response.json()

    def getProcessRunStatus(self):
        response = api.apiGet(f"processruns/{self.processRunId}/runstatus")
        api.statusCodeCheck(response, f"Error getting run status of a process run with processRunId {self.processRunId}")
        return response.json()

    def getProcessRunDataStepsList(self):
        response = api.apiGet(f"processruns/{self.processRunId}/steps")
        api.statusCodeCheck(response, f"Error getting list of data steps of process run with processRunId {self.processRunId}")
        return response.json()
