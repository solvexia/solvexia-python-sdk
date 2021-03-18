#!/usr/bin/env python

class process:
    def __init__self(self, authorisation, processId);
        self._authorisation = authorisation
        self._processId = processId
        self._baseurl = "https:///app.solvexia.com/api/v1/processes"
    
    def process_list(self):
        response = requests.get(self._baseurl, headers=self_.authorisation)
        if response.status_code != 200:
            print("Error getting process list")
            sys.exit()
        return response.json()
    
    def get_process(self):
        get_process_url = self._baseurl + f'/{self._processId}'
        response = requests.get(get_process_url, headers=self_.authorisation)
        if response.status_code != 200:
            print("Error getting chosen process")
            sys.exit()
        return response.json()

    def create_process_run(self):
        create_process_run_url = self._baseurl + f'/{self._processID}/processruns'
        response = requests.post(create_process_run_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error creating process run")
            sys.exit()
        return response.json()

    def process_run_list(self):
        process_run_url = self._baseurl + f'/{self._processID}/processruns'
        response = requests.get(process_run_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error getting process run list")
            sys.exit()
        return response.json()
    
    def process_data_step_list(self):
        process_data_step_url = self._baseurl + f'/{self._processID}/steps'
        response = requests.get(process_data_step_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error getting data step list")
            sys.exit()
        return response.json()