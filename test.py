#!/usr/bin/env python

from solvexia_sdk import api
from solvexia_sdk.file import file
from solvexia_sdk.process import process
from solvexia_sdk.processrun import processrun
from solvexia_sdk.datasteps import datasteps
from solvexia_sdk.table import table

client = api.solvexia_client("CDA77AD1-168D-EB11-82D5-000D3AD127EB", "fsORNx&Y61eAn3PpE2%", "volibear.qa")
client.getAccessToken()

# TESTING ALL FILE API CALLS

# fileTest = file.file("f-5922731")
# fileTest.getFileMetadata() 
# fileTest.updateMetadata("Thisisatest.csv")
# fileTest.downloadFile()
# fileTest.uploadFile("Upload-test.csv")
# fileTest.startChunkSession()
# fileTest.uploadChunk(100, "CollectedClientResponse.csv")
# fileTest.commitUpload()
# fileTest.uploadFileByChunks(100, "CollectedClientResponse.csv")

# TESTING ALL PROCESSRUN API CALLS
# ALL WORK AS INTENDED

# processRunTest = processrun.processruns("pr-5916704")
# processRunTest.getProcessRun()
# processRunTest.getProcessStatus()
# processRunTest.cancelProcessRun()
# processRunTest.getProcessStatus()
# processRunTest.getProcessRunDataSteps()
# processRunTest.startProcessRun()

# TESTING ALL PROCESS API CALLS
# ALL WORK BUT NOT SURE ABOUT THE TIME FILTER FOR GETPROCESSLIST

# processTest = process.process("p-5854642")
# processTest.getProcessList()
# processTest.getProcess()
# processTest.createProcessRun("hello bob")
# processTest.getProcessRunList()
# processTest.getProcessDataStepList()

# TESTING DATA STEP API CALLS
# ALL WORK AS INTENDED

# dataStepsTest = datasteps.datasteps("ds-5854643")
# dataStepsTest.getDataStep()
# dataStepsTest.getDataStepProperties()
# dataStepsTest.getDataStepPropertyForDataStep("dsprop-1844675")
# payload = {
#     'file': 'f-5854647', 
#     'id': 'dsprop-1844675', 
#     'name': 'Source File Renamed', 
#     'dataType': 'File', 
#     'required': False, 
#     'visible': True, 
#     'informationFlowType': 'INPUT', 
#     'mouseoverText': ''
#     }
# dataStepsTest.updateDataStepProperty("dsprop-1844675", payload)
# dataStepsTest.getDataStepPropertyForDataStep("dsprop-1844675")

# TESTING ALL TABLE API CALLS
# ALL WORK AS INTENDED

# tableTest = table.table("mt-5922660")
# tableTest.getTable()
# tableTest.createTable("newName12", "newDescription")
# tableTest.updateTable("newName14", "newDescription")
# tableTest.getTableColumns()
# payload = {
#     'name': "HelloThere5",
#     'dataType': "number"
# }
# tableTest.createColumn(payload)
# tableTest.getTableColumns()
# tableTest.updateColumn(payload, "HelloThere3")
# tableTest.deleteColumn("HelloThere5")
# tableTest.getTableColumns()
# This one is generating an error, I believe this is due to permissions so I will recheck in a bit
# tableTest.createColumn(payload)
# Same problem with the remaining column functions
# Create a new managed table and retest this