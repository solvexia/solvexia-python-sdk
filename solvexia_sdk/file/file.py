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

    def getFileMetadata(self):
        response = api.apiGet(f"files/{self.fileId}/metadata")
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
        uploadFileUrl = api.baseUrl + f"files/{self.fileId}"
        with open(file, "rb") as openFile:
            response = requests.post(uploadFileUrl, files={"Filename": openFile}, headers=api.access_token)
        api.statusCodeCheck(response, "Error uploading file")
        print(response.json())
        return response.json()

    def downloadFile(self):
        downloadFileUrl = api.baseUrl + f"files/{self.fileId}"
        headers = api.access_token
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.get(downloadFileUrl, headers=headers)
        api.statusCodeCheck(response, "Error downloading file")
        return response

    def startChunkSession(self):
        response = api.apiPostNoPayload(f"files/{self.fileId}/uploadsessions")
        api.statusCodeCheck(response, "Error starting chunk session")
        self.uploadSessionId = response.json()['uploadsessionid']
        self.chunkId = 1

    def uploadChunk(self, chunkSize, file):
        # TO DO
        fileSize = os.stat(file).st_size
        numOfChunks = math.ceil(fileSize/chunkSize)

        fs = Filesplit()
        fs.split(file=file, split_size=chunkSize)
        filename = os.path.basename(file)
        fileExtension = os.path.splitext(file)[1]

        while self.chunkId <= numOfChunks:
            uploadChunkUrl = api.baseUrl + f"files/{self.fileId}/uploadsessions/{self.uploadSessionId}/chunks/{self.chunkId}"
            with open(os.path.splitext(file)[0] + f"_{self.chunkId}{fileExtension}", 'rb') as f:
                response = requests.post(uploadChunkUrl, files={file: f}, headers=api.access_token)
            api.statusCodeCheck(response, "Error spliting and uploading file chunk")
            self.chunkId = self.chunkId + 1
        

    def commitUpload(self):
        response = api.apiPostNoPayload(f"files/{self.fileId}/uploadsessions/{self.uploadSessionId}/commit")
        api.statusCodeCheck(response, "Error committing file upload")
        print(response.json())
        return response.json()

    def uploadFileByChunks(self, chunkSize, file):
        self.startChunkSession()
        self.uploadChunk(chunkSize, file)
        self.commitUpload()