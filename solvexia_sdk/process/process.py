#!/usr/bin/env python
import requests
import json
import sys
from solvexia_sdk import api

class process:
    def __init__(self, processId);
        self.processId = processId
    
    def getProcessList(self):
        response = api.apiGet("processes")
        api.statusCodeCheck(response, "Error getting process list")
        return response.json()
    
    def getProcess(self):
        response = api.apiGet(f"processes/{self.processId}")
        api.statusCodeCheck(response, "Error getting chosen process")
        return response.json()

    def createProcessRun(self):
        response = api.apiPostNoPayload(f"processes/{self.processId}/processruns")
        api.statusCodeCheck(response, "Error creating process run")
        return response.json()

    def getProcessRunList(self):
        response = api.apiGet(f"processes/{self.processId}/processruns")
        api.statusCodeCheck(response, "Error getting run list")
        return response.json()
    
    def getProcessDataStepList(self):
        response = api.apiGet(f"processes/{self.processId}/steps")
        api.statusCodeCheck(response, "Error getting data step list")
        return response.json()