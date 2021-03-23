#!/usr/bin/env python

import requests
import json
import sys

class file:
    def __init__(self, authorisation, fileId):
        self.authorisation = authorisation
        self.fileId = fileId
        self.baseUrl = "https:///app.solvexia.com/api/v1/files/"

    def fileMetadata(self):
        metadataUrl = self.baseUrl + f"{self._fileId}/metadata"
        response = requests.get(metadataUrl, headers=self.authorisation)
        if response.status_code() != 200:
            print("Error getting meta data for file")
            sys.exit()
        return response.json()

    def updateMetadata(self, name):
        metadataUrl = self.baseUrl + f"{self.fileId}/metadata"
        payload = {
            'name': name
        }
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(metadataUrl, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Error updating file metadata")
            sys.exit()
        return response.json()

    def uploadFile(self, file):
    # TO DO
        uploadFileUrl = self.baseUrl + fileId
        with open(file, 'rb') as f:
            response = requests.post(uploadFileUrl, files={file: f})
        if response.status_code != 200:
            print("Error uploading file")
            sys.exit()
        return response.json()

    def downloadFile(self):
        downloadFileUrl = self.baseUrl + self.fileId
        headers = self.authorisation
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.get(downloadFileUrl, headers=headers)
        if response.status_code != 200:
            print("Error downloading file")
            sys.exit()
        return response

    def startChunkSession(self):
        startChunkUrl = self.baseUrl + f"{fileId}/uploadsessions"
        response = response.post(startChunkUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error starting chunk session")
            sys.exit()
        self.uploadSessionId = response.json()['uploadSessionId']
        self.chunkId = 1

    def uploadChunk(self, uploadSessionId, chunkId):
        # TO DO

    def commitChunkUpload(self):
        commitChunkUrl = self.baseUrl + f"{self.fileId}/uploadsessions/{self.uploadSessionId}/commit"
        response = requests.post(commitChunkUrl, headers=self.authorisation)
        if response.status_code != 200:
            print("Error committing chunk upload")
            sys.exit()
        return response.json()