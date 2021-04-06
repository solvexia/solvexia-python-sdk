#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class processRuns:
    def __init__(self, processRunId):
        self.processRunId = processRunId

    def get_process_run(self):
        response = api.api_get(f"processruns/{self.processRunId}")
        api.status_code_check(response, f"Error getting the specified process run with processRunId {self.processRunId}")
        return response.json()
    
    def start_process_run(self):
        payload = {
            'request': 'ProcessRun_StartRq',
            'processRunId': self.processRunId
        }
        response = api.api_post("requests", payload)
        api.status_code_check(response, f"Error starting process run with processRunId {self.processRunId}")
        return response.json()

    def cancel_process_run(self):
        payload = {
            'request': 'ProcessRun_CancelRq',
            'processRunId': self.processRunId
        }
        response = api.api_post("requests", payload)
        api.status_code_check(response, f"Error cancelling process run with processRunId {self.processRunId}")
        return response.json()

    def get_process_run_status(self):
        response = api.api_get(f"processruns/{self.processRunId}/runstatus")
        api.status_code_check(response, f"Error getting run status of a process run with processRunId {self.processRunId}")
        return response.json()

    def get_process_run_data_steps_list(self):
        response = api.api_get(f"processruns/{self.processRunId}/steps")
        api.status_code_check(response, f"Error getting list of data steps of process run with processRunId {self.processRunId}")
        return response.json()
