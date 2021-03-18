#!/usr/bin/env python

class file:
    def __init__(self, authorisation, fileId):
        self._authorisation = authorisation
        self._fileId = fileId
        self._baseurl = "https:///app.solvexia.com/api/v1/files/"

    def file_metadata(self):
        metadata_url = self._baseurl + f'{self._fileId}/metadata'
        response = requests.get(metadata_url, headers=self._authorisation)
        if response.status_code() != 200:
            print("Error getting meta data for file")
            sys.exit()
        return response.json()

    def update_metadata(self, name):
        metadata_url = self._baseurl + f'{self._fileId}/metadata'
        payload = {
            'name': name
        }
        headers = self._authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(metadata_url, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Error updating file metadata")
            sys.exit()
        return response.json()

    def upload_file(self, file):
    # TO DO
        upload_file_url = self._baseurl + fileId
        with open(file, 'rb') as f:
            response = requests.post(upload_file_url, files={file: f})
        if response.status_code != 200:
            print("Error uploading file")
            sys.exit()
        return response.json()

    def download_file(self):
        download_file_url = self._baseurl + self._fileId
        # headers = self._authorisation
        # headers['Content-Type'] = 'application/octet-stream'
        response = requests.get(download_file_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error downloading file")
            sys.exit()
        return response

    def start_chunk_session(self):
        start_chunk_url = self._baseurl + f'{fileId}/uploadsessions'
        response = response.post(start_chunk_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error starting chunk session")
            sys.exit()
        return response.json()

    def upload_chunk(self, uploadSessionId, chunkId):
        # TO DO

    def commit_chunk_upload(self, uploadSessionId):
        commit_chunk_url = self._baseurl + f'{self._fileId}/uploadsessions/{uploadSessionId}/commit'
        response = requests.post(commit_chunk_url, headers=self._authorisation)
        if response.status_code != 200:
            print("Error committing chunk upload")
            sys.exit()
        return response.json()