#!/usr/bin/env python

from solvexia_sdk import api
from solvexia_sdk.file import file
from solvexia_sdk.process import process
from solvexia_sdk.processrun import processrun
from solvexia_sdk.datasteps import datasteps
from solvexia_sdk.table import table

client = api.solvexia_client("CDA77AD1-168D-EB11-82D5-000D3AD127EB", "fsORNx&Y61eAn3PpE2%", "volibear.qa")
client.getAccessToken()

# All these work as intended however not sure how to test download and upload
"""fileTest = file.file("f-5854647")
fileTest.getFileMetadata() 
fileTest.updateMetadata("Thisisatest.csv")
fileTest.downloadFile()"""

# All these work as intended
processRunTest = processrun.processruns("pr-5916704")
"""processRunTest.getProcessRun()
processRunTest.getProcessStatus()
processRunTest.cancelProcessRun()
processRunTest.getProcessStatus()
processRunTest.getProcessRunDataSteps()
processRunTest.startProcessRun()"""

processTest = process.process("p-5854642")
# All work as intended
# Still need to test by adding query parameters to getProcessList()
"""processTest.getProcessList()
processTest.getProcess()
processTest.createProcessRun("hello bob")
processTest.getProcessRunList()
processTest.getProcessDataStepList()"""


# Theses all work but need to test dataStepProperties because
# I am unsure of how to get dataStepPropertiesId
"""dataStepsTest = datasteps.datasteps("ds-5854643")
dataStepsTest.getDataStep()
dataStepsTest.getDataStepProperties()
dataStepsTest.getDataStepPropertyForDataStep()"""

tableTest = table.table("mt-4970934")
"""tableTest.getTable()
tableTest.createTable("newName3", "newDescription")
tableTest.updateTable("newName4", "newDescription")"""
tableTest.getTableColumns()
payload = {
    'name': "HelloThere",
    'dataType': "TableColumDataType"
}
# This one is generating an error, I believe this is due to permissions so I will recheck in a bit
# tableTest.createColumn(payload)
# Same problem with the remaining column functions
# Create a new managed table and retest this