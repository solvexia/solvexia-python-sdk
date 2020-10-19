#Functions Sandbox#
import requests
import sys
import json
import sys
import os
from fsplit.filesplit import FileSplit
import math

class solvexia_client:
    def __init__(self, config_path):
        with open(config_path) as config:
            param = json.load(config)
            self.env = param["env"]
            self.client_id = param["client_id"]
            self.client_secret = param["client_secret"]

#Define Access Token Retrieval Function#
    def req(self):
        pload = {'client_id': self.client_id,
                 'client_secret': self.client_secret, 'grant_type': 'client_credentials'}
        urlr = self.env + '/oauth/token'
        r = requests.post(urlr, data=pload)
        if r.status_code != 200:
            print("Error with Generating an Access Token via Client Credential Flow")
            sys.exit()
        ra = r.json()['access_token']
        rat = 'Bearer ' + ra  # rat stands for 'Request Access Token'#
        hload = {'Authorization': rat}
        return hload

#Define API Get Function#
    def svx_api_get(self, url):
        hload = self.req()
        resp = requests.get(self.env + url, headers=hload)
        if resp.status_code != 200:
            print("Error with API Get Function")
            sys.exit()
        return resp

#Define API Post Function#
    def svx_api_post(self, url, *args, **kwargs):
        filename = kwargs.get('filename', None)
        pr = kwargs.get('pr', None)
        hload = self.req()
        if (filename is None and pr is None):
            resp = requests.post(self.env + url, headers=hload)
            if resp.status_code != 200:
                print("Error with Creating a Process Run")
                sys.exit()
            return resp
        elif (filename is not None and pr is None):
            files = {'file': open(str(filename) + '.xlsx', 'rb')}
            resp = requests.post(self.env + url, headers=hload, files=files)
            if resp.status_code != 200:
                print("Error with Uploading a File")
            return resp
        elif (filename is None and pr is not None):
            rpr1load = {'request': 'ProcessRun_StartRq', 'processRunId': pr}
            resp = requests.post(self.env + url, headers=hload, json=rpr1load)
            if resp.status_code != 200:
                print("Error with Starting a Process Run")
            return resp

    #Define Create a Process Run Function#
    def svx_create_processrun(self, processname):
        urlp1 = '/api/v1/processes'
        rp1 = self.svx_api_get(urlp1)

        i = 0
        while i < len(rp1.json()):
            a = rp1.json()[i]['name']
            if a == processname:
                break
            i = i+1
        prcs = rp1.json()[i]['id']
        urlpr1 = '/api/v1/processes/' + prcs + '/processruns'
        rpr1 = self.svx_api_post(urlpr1)
        return rpr1.json()

    #Define Upload a File Function#
    def svx_upload_file(self, pr, stepname, filename):
        urlp1 = '/api/v1/processruns/' + pr + '/steps'
        rp1 = self.svx_api_get(urlp1)

        g = 0
        while g < len(rp1.json()):
            if rp1.json()[g]['name'] == str(stepname):
                break
            g = g+1
        stepid = rp1.json()[g]['id']
        urlp2 = '/api/v1/steps/' + stepid + '/properties'
        rp2 = self.svx_api_get(urlp2)
        fileid = rp2.json()[0]['file']
        urlf1 = '/api/v1/files/' + fileid
        rf1 = self.svx_api_post(urlf1, filename=filename)
        print(rf1.json())

#Define Start a Process Run Function#
    def svx_start_process(self, pr, time):
        urlpr1 = '/api/v1/requests'
        rpr1 = self.svx_api_post(urlpr1, pr=pr)
        print(rpr1.json())
        urlpr2 = '/api/v1/processruns/'+pr+'/runstatus'
        rpr2 = self.svx_api_get(urlpr2)
        print(rpr2.json())
        process_run_status = rpr2.json()['status']
        while process_run_status == 'Running':
            rpr2 = self.svx_api_get(urlpr2)
            print(rpr2.json())
            process_run_status = rpr2.json()['status']
            if rpr2.json()['runDurationInSeconds'] > time:
                print("Process Run took too long")
                process_run_status = 'Failed'
                break
        return process_run_status

    def file_upload_chunks(self, file_path, file_id, chunk_size):

        

        #get file size#
        size = os.stat(file_path).st_size

        #Create Chunk Session#
        uploadsession_url = '/api/v1/files/' + file_id + '/uploadsessions'
        create_uploadsession_res = self.svx_api_post(uploadsession_url)
        uploadsession_id = create_uploadsession_res.json()['uploadsessionid']

        if create_uploadsession_res.status_code != 200:
            print("Error occured while creating a chunk session {}",
                  create_uploadsession_res.json().message)
            sys.exit()
        print(create_uploadsession_res.json())


        #Split File into Chunks#
        fs = FileSplit(file=file_path, splitsize=chunk_size)
        fs.split(callback=split_cb)
        
        global i = 1
        def split_cb(f, s):
          print("file: {0}, size: {1}".format(f, s))
          upload_chunk_url = '/api/v1/files/' + f + '/uploadsessions/' + \
                uploadsession_id + '/chunks/' + str(i)
          files = {'file': open(f, 'rb')}
          upload_chunk_res = self.svx_api_post(upload_chunk_url, files=files)
          i = i + 1

          if upload_chunk_res.status_code != 200:
              print("Error with Uploading Chunk ID " + str(i) +
                    "Error: {}", upload_chunk_res.json().message)
              sys.exit()
          print(upload_chunk_res.json())

        # #Upload Chunks#
        # i = 1
        # while i < math.ceil(size/chunk_size) + 1:
        #     upload_chunk_url = '/api/v1/files/' + file_id + '/uploadsessions/' + \
        #         uploadsession_id + '/chunks/' + str(i)
        #     files = {'file': open(file_path + str(i) + '.xlsx', 'rb')}
        #     upload_chunk_res = self.svx_api_post(upload_chunk_url, files=files)

        #     if upload_chunk_res.status_code != 200:
        #         print("Error with Uploading Chunk ID " + str(i) +
        #               "Error: {}", upload_chunk_res.json().message)
        #         sys.exit()
        #     print(upload_chunk_res.json())
        #     i = i + 1

        #Commit Chunk Session#
        commit_uploadsession_url = '/api/v1/files/' + file_id + '/uploadsessions/' + uploadsession_id + '/commit'
        commit_uploadsession_res = self.svx_api_post(commit_uploadsession_url)

        if commit_uploadsession_res.status_code != 200:
            print("Error with Commiting the Chunking Session: {}",
                  commit_uploadsession_res.json().message)
            sys.exit()
        print(commit_uploadsession_res.json())

        #Rename Chunked File#
        update_file_url = '/api/v1/files/' + file_id + '/metadata'
        update_file_req = {'name': 'Derek Test List Wages Chunked.xlsx'}
        update_file_res = self.svx_api_post(update_file_url, json=update_file_req)
        if update_file_res.status_code != 200:
            print("Error with Renaming the Chunked File: {}",
                  update_file_res.json().message)
            sys.exit()
        print(update_file_res.json())
