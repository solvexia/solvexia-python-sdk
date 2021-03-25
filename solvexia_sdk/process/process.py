#!/usr/bin/env python
import requests
import json
import sys
from solvexia_sdk import api

class process:
    def __init__(self, processId);
        self.processId = processId
    
    def getProcessList(self, name=None, dateCreatedStart=None, dateCreatedEnd=None):
        params = {
            'name': name,
            'dateCreatedStarted': dateCreatedStart,
            'dateCreatedEnd': dateCreatedEnd
        }
        response = requests.get(api.baseUrl + "processes", params=params, headers=api.access_token)
        api.statusCodeCheck(response, "Error getting process list")
        return response.json()
    
    def getProcess(self):
        response = api.apiGet(f"processes/{self.processId}")
        api.statusCodeCheck(response, "Error getting chosen process")
        return response.json()

    def createProcessRun(self, optionalName=None):
        if optionalName is None:
            response = api.apiPostNoPayload(f"processes/{self.processId}/processruns")
        else:
            payload = {
                'namePrefix': optionalName
            }
            response = api.apiPost(f"processes/{self.processId}/processruns", payload)
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