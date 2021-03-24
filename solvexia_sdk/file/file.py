#!/usr/bin/env python

import requests
import json
import sys
import math
import os
from fsplit.filesplit import Filesplit
from solvexia_sdk import api

class file:
    def __init__(self, fileId):
        self.fileId = fileId
        self.baseUrl = "https:///app.solvexia.com/api/v1/files/"

    def getFileMetadata(self):
        metadataUrl = self.baseUrl + f"{self._fileId}/metadata"
        response = requests.get(metadataUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting metadata for file")
        return response.json()

    def updateMetadata(self, name):
        payload = {
            'name': name
        }
        response = api.apiPost(f"files/{self.fileId}/metadata", payload)
        api.statusCodeCheck(response, "Error updating file metadata")
        return response.json()

    def uploadFile(self, file):
    # TO DO
        uploadFileUrl = api.baseUrl + f"files/{self.fileId}"
        with open(file, 'rb') as f:
            response = requests.post(uploadFileUrl, files={file: f}), headers=self.authorisation
            api.statusCodeCheck(response, "Error uploading file")
        return response.json()

    def downloadFile(self):
        downloadFileUrl = self.baseUrl + self.fileId
        headers = self.authorisation
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.get(downloadFileUrl, headers=headers)
        api.statusCodeCheck(response, "Error downloading file")
        return response

    def startChunkSession(self):
        response = apiPostNoPayload(f"files/{self.fileId}/uploadsessions")
        api.statusCodeCheck(response, "Error starting chunk session")
        self.uploadSessionId = response.json()['uploadSessionId']
        self.chunkId = 1

    def uploadChunk(self, chunkSize, file):
        # TO DO
        fileSize = os.stat(file).st_size
        numOfChunks = math.ceil(fileSize/chunkSize)

        fs = FileSplit(file=file, fileSize=chunkSize)
        fs.split()
        filename = os.path.basename(file)
        fileExtension = os.path.splitext(file)[1]

        while self.chunkId <= numOfChunks:
            uploadChunkUrl = self.baseUrl + f"{self.fileId}/uploadsessions/{self.uploadSessionId}/chunks/{self.chunkId}"
            with open(file + f"_{chunkId}{fileExtension}", 'rb') as f:
                response = requests.post(uploadChunkUrl, files={file: f}, headers=self.authorisation)
            api.statusCodeCheck(response, "Error spliting and uploading file chunk")
            self.chunkId = self.chunkId + 1
        

    def commitUpload(self):
        response = api.apiPostNoPayload(f"files/{self.fileId}/uploadsessions/{self.uploadSessionId}/commit")
        api.statusCodeCheck(response, "Error committing file upload")
        return response.json()

    def uploadFileByChunks(self, chunkSize, file)
        startChunkSession(self)
        uploadChunk(self, chunkSize, file)
        commitUpload(self)