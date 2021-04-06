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

    def get_file_metadata(self):
        response = api.api_get(f"files/{self.fileId}/metadata")
        api.status_code_check(response, f"Error getting metadata for file with fileId {self.fileId}")
        return response.json()

    def update_file_metadata(self, name):
        payload = {
            'name': name
        }
        response = api.api_post(f"files/{self.fileId}/metadata", payload)
        api.status_code_check(response, f"Error updating metadata for file with fileId {self.fileId}")
        return response.json()

    def upload_file(self, file):
        uploadFileUrl = api.baseUrl + f"files/{self.fileId}"
        with open(file, "rb") as openFile:
            response = requests.post(uploadFileUrl, files={"Filename": openFile}, headers=api.accessToken)
        api.status_code_check(response, f"Error uploading file {file}")
        return response.json()

    def download_file(self):
        downloadFileUrl = api.baseUrl + f"files/{self.fileId}"
        headers = api.accessToken
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.get(downloadFileUrl, headers=headers)
        api.status_code_check(response, f"Error downloading file with fileId {self.fileId}")
        return response

    def start_upload_session(self):
        response = api.api_post_no_payload(f"files/{self.fileId}/uploadsessions")
        api.status_code_check(response, f"Error starting upload session for file with fileId {self.fileId}")
        self.uploadSessionId = response.json()['uploadsessionid']
        self.chunkId = 1

    def upload_chunk(self, chunkSize, file):
        fileSize = os.stat(file).st_size
        numOfChunks = math.ceil(fileSize/chunkSize)

        fs = Filesplit()
        fs.split(file=file, split_size=chunkSize)
        filename = os.path.basename(file)
        fileExtension = os.path.splitext(file)[1]

        while self.chunkId <= numOfChunks:
            uploadChunkUrl = api.baseUrl + f"files/{self.fileId}/uploadsessions/{self.uploadSessionId}/chunks/{self.chunkId}"
            with open(os.path.splitext(file)[0] + f"_{self.chunkId}{fileExtension}", 'rb') as f:
                response = requests.post(uploadChunkUrl, files={file: f}, headers=api.accessToken)
            api.status_code_check(response, f"Error spliting and uploading file with fileId {self.fileId} and chunkId {self.chunkId}")
            self.chunkId = self.chunkId + 1
        
    def commit_upload(self):
        response = api.api_post_no_payload(f"files/{self.fileId}/uploadsessions/{self.uploadSessionId}/commit")
        api.status_code_check(response, f"Error committing upload for file with fileId {self.fileId}")
        return response.json()

    def upload_file_by_chunks(self, chunkSize, file):
        self.start_upload_session()
        self.upload_chunk(chunkSize, file)
        self.commit_upload()