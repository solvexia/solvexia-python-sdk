#!/usr/bin/env python

import requests
import json
import sys
import math
import os
from fsplit.filesplit import Filesplit
from solvexia_sdk import helper

class file:
    def __init__(self, authorisation, fileId):
        self.authorisation = authorisation
        self.fileId = fileId
        self.baseUrl = "https:///app.solvexia.com/api/v1/files/"

    def fileMetadata(self):
        metadataUrl = self.baseUrl + f"{self._fileId}/metadata"
        response = requests.get(metadataUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting metadata for file")
        return response.json()

    def updateMetadata(self, name):
        metadataUrl = self.baseUrl + f"{self.fileId}/metadata"
        payload = {
            'name': name
        }
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(metadataUrl, data=json.dumps(payload), headers=headers)
        helper.statusCodeCheck(response, "Error updating file metadata")
        return response.json()

    def uploadFile(self, file):
    # TO DO
        uploadFileUrl = self.baseUrl + fileId
        with open(file, 'rb') as f:
            response = requests.post(uploadFileUrl, files={file: f}), headers=self.authorisation
            helper.statusCodeCheck(response, "Error uploading file")
        return response.json()

    def downloadFile(self):
        downloadFileUrl = self.baseUrl + self.fileId
        headers = self.authorisation
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.get(downloadFileUrl, headers=headers)
        helper.statusCodeCheck(response, "Error downloading file")
        return response

    def startChunkSession(self):
        startChunkUrl = self.baseUrl + f"{fileId}/uploadsessions"
        response = response.post(startChunkUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error starting chunk session")
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
            helper.statusCodeCheck(response, "Error spliting and uploading file chunk")
            self.chunkId = self.chunkId + 1
        

    def commitUpload(self):
        commitUrl = self.baseUrl + f"{self.fileId}/uploadsessions/{self.uploadSessionId}/commit"
        response = requests.post(commitUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error committing chunk upload")
        return response.json()