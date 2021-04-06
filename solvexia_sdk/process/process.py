#!/usr/bin/env python
import requests
import json
import sys
from solvexia_sdk import api

class process:
    def __init__(self, process_id):
        self.process_id = process_id
    
    def get_process_list(self, name=None, date_created_start=None, date_created_end=None):
        params = {
            'name': name,
            'dateCreatedStarted': date_created_start,
            'dateCreatedEnd': date_created_end
        }
        response = requests.get(api.base_url + "processes", params=params, headers=api.accessToken)
        api.status_code_check(response, "Error getting process list")
        return response.json()
    
    def get_process(self):
        response = api.api_get(f"processes/{self.process_id}")
        api.status_code_check(response, f"Error getting process with process_id {self.process_id}")
        return response.json()

    def create_process_run(self, optional_name=None):
        if optional_name is None:
            response = api.api_post_no_payload(f"processes/{self.process_id}/processruns")
        else:
            payload = {
                'namePrefix': optional_name
            }
            response = api.api_post(f"processes/{self.process_id}/processruns", payload)
        api.status_code_check(response, f"Error creating process run with process_id {self.process_id}")
        return response.json()

    def get_process_run_list(self):
        response = api.api_get(f"processes/{self.process_id}/processruns")
        api.status_code_check(response, f"Error getting process run list with process_id {self.process_id}")
        return response.json()
    
    def get_process_data_step_list(self):
        response = api.api_get(f"processes/{self.process_id}/steps")
        api.status_code_check(response, f"Error getting process data step list with process_id {self.process_id}")
        return response.json()