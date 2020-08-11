import sys
import os
from fsplit.filesplit import FileSplit
import requests
import math

def file_upload_chunks(file, file_id, chunk_size):

    #Split File into Chunks#
    fs = FileSplit(file=file, splitsize=chunk_size)
    fs.split()

    #get file size#
    size = os.stat('Derek Test List Wages.xlsx').st_size
    
    #Create Chunk Session#
    uploadsession_url = 'https://' + Env + '.qa.solvexia.com/api/v1/files/' + file_id + '/uploadsessions'
    create_uploadsession_res = requests.post(uploadsession_url, headers=hload)
    uploadsession_id = create_uploadsession_res.json()['uploadsessionid']
    
    if create_uploadsession_res.status_code != 200:
        print("Error occured while creating a chunk session {}", create_uploadsession_res.json().message)
        sys.exit()
    print(create_uploadsession_res.json())

    #Upload Chunks#
    i = 1
    while i < math.ceil(size/chunk_size) + 1:
        upload_chunk_url = 'https://' + Env + '.qa.solvexia.com/api/v1/files/' + \
            file_id + '/uploadsessions/' + uploadsession_id + '/chunks/' + str(i)
        files = {'file': open('Derek Test List Wages_' + str(i) + '.xlsx', 'rb')}
        upload_chunk_res = requests.post(upload_chunk_url, headers=hload, files=files)
        
        if upload_chunk_res.status_code != 200:
            print("Error with Uploading Chunk ID " + str(i) + "Error: {}", upload_chunk_res.json().message)
            sys.exit()
        print(upload_chunk_res.json())
        i = i + 1

    #Commit Chunk Session#
    commit_uploadsession_url = 'https://' + Env + '.qa.solvexia.com/api/v1/files/' + \
        file_id + '/uploadsessions/' + uploadsession_id + '/commit'
    commit_uploadsession_res = requests.post(commit_uploadsession_url, headers=hload)
    
    if commit_uploadsession_res.status_code != 200:
        print("Error with Commiting the Chunking Session: {}", commit_uploadsession_res.json().message)
        sys.exit()
    print(commit_uploadsession_res.json())

    #Rename Chunked File#
    update_file_url = 'https://' + Env + '.qa.solvexia.com/api/v1/files/' + file_id + '/metadata'
    update_file_req = {'name': 'Derek Test List Wages Chunked.xlsx'}
    update_file_res = requests.post(update_file_url, headers=hload, json=update_file_req)
    if update_file_res.status_code != 200:
        print("Error with Renaming the Chunked File: {}", update_file_res.json().message)
        sys.exit()
    print(update_file_res.json())