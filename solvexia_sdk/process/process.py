#!/usr/bin/env python
import requests
import json
import sys
from solvexia_sdk import api

class process:
    def __init__(self, processId):
        self.processId = processId
    
    def get_process_list(self, name=None, dateCreatedStart=None, dateCreatedEnd=None):
        params = {
            'name': name,
            'dateCreatedStarted': dateCreatedStart,
            'dateCreatedEnd': dateCreatedEnd
        }
        response = requests.get(api.baseUrl + "processes", params=params, headers=api.accessToken)
        api.status_code_check(response, "Error getting process list")
        return response.json()
    
    def get_process(self):
        response = api.api_get(f"processes/{self.processId}")
        api.status_code_check(response, f"Error getting process with processId {self.processId}")
        return response.json()

    def create_process_run(self, optionalName=None):
        if optionalName is None:
            response = api.api_post_no_payload(f"processes/{self.processId}/processruns")
        else:
            payload = {
                'namePrefix': optionalName
            }
            response = api.api_post(f"processes/{self.processId}/processruns", payload)
        api.status_code_check(response, f"Error creating process run with processId {self.processId}")
        return response.json()

    def get_process_run_list(self):
        response = api.api_get(f"processes/{self.processId}/processruns")
        api.status_code_check(response, f"Error getting process run list with processId {self.processId}")
        return response.json()
    
    def get_process_data_step_list(self):
        response = api.api_get(f"processes/{self.processId}/steps")
        api.status_code_check(response, f"Error getting process data step list with processId {self.processId}")
        return response.json()