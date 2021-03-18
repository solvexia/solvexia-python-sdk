#!/usr/bin/env python

class processruns:
    def __init__self(self, authorisation, processRunId);
        self._authorisation = authorisation
        self._processRunId = processRunId
        self._baseurl = "https:///app.solvexia.com/api/v1/"

    def get_process_run(self):
        get_process_run_url = self._baseurl + f'processruns/{self._processRunId}'
        response = requests.get(get_process_run_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error getting the specified process run")
            sys.exit()
        return response.json()
    
    def start_process_run(self):
        start_process_run_url = self.baseurl + 'requests'
        payload = {
            'request': 'ProcessRun_StartRq',
            'processRunId': self._processRunId
        }
        headers = self._authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(start_process_run_url, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Error starting process run")
            sys.exit()
        return response.json()

    def cancel_process_run(self):
        cancel_process_run_url = start_process_run_url = self.baseurl + 'requests'
        payload = {
            'request': 'ProcessRun_CancelRq',
            'processRunId': self._processRunId
        }
        headers = self._authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(cancel_process_run_url, data=json.dumps(payload), headers=headers)
        if response.status_code() != 200:
            print("Error cancelling process run")
            sys.exit()
        return response.json()

    def process_status(self):
        process_status_url = self._baseurl + f'processruns/{self._processRunId}/runstatus'
        response = requests.get(process_status_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error getting run status of a process run")
            sys.exit()
        return response.json()

    def process_run_data_steps(self):
        process_date_steps_url = self._baseurl + f'processruns/{self._processRunId}/steps'
        response = requests.get(process_date_steps_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error getting list of data steps")
            sys.exit()
        return response.json()
