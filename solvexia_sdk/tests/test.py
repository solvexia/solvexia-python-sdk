from solvexia_sdk import api
from solvexia_sdk.file import file
from solvexia_sdk.process import process
from solvexia_sdk.processrun import processrun
from solvexia_sdk.datasteps import datasteps
from solvexia_sdk.table import table

client = api.solvexiaClient("auth.json")
client.get_access_token()

processTest = process.process("p-41423")
response = processTest.get_process_run_list(None, "2021-05-11T03:30:43.297")
print(response)

'''processTest = process.process("p-37817")
final_file_list = processTest.get_process_file_list()

dataStepsTest = datasteps.dataSteps("ds-37818")
test_list = dataStepsTest.get_data_step_file_list()
    
print(final_file_list)
print(test_list)

fileTest = file.file("f-5940022")
fileTest.get_file_metadata() 
fileTest.upload_file("Upload-test.csv")
fileTest.update_file_metadata("Thisisatest.csv")
fileTest.download_file()
fileTest.start_upload_session()
fileTest.upload_chunk(100, "CollectedClientResponse.csv")
fileTest.commit_upload()
fileTest.upload_file_by_chunks(100, "CollectedClientResponse.csv")

processRunTest = processrun.processRuns("pr-5916704")
processRunTest.get_process_run()
processRunTest.get_process_run_status()
processRunTest.get_process_run_data_steps_list()
processRunTest.start_process_run()
processRunTest.cancel_process_run()


processTest = process.process("p-5854642")
processTest.get_process_list()
processTest.get_process()
processTest.create_process_run("hello bob")
processTest.get_process_run_list()
processTest.get_process_data_step_list()


dataStepsTest = datasteps.dataSteps("ds-5854643")
dataStepsTest.get_data_step()
dataStepsTest.get_data_step_property_list()
dataStepsTest.get_data_step_property_for_data_step("dsprop-1844675")
payload = {
    'file': 'f-5854647', 
    'id': 'dsprop-1844675', 
    'name': 'Source File Renamed', 
    'dataType': 'File', 
    'required': False, 
    'visible': True, 
    'informationFlowType': 'INPUT', 
    'mouseoverText': ''
    }
dataStepsTest.update_data_step_property("dsprop-1844675", payload)
dataStepsTest.get_data_step_property_for_data_step("dsprop-1844675")


tableTest = table.table("mt-5922660")
tableTest.get_table()
tableTest.create_table("newName12", "newDescription")
tableTest.update_table("newName14", "newDescription")
tableTest.get_table_columns_list()
payload = {
    'name': "HelloThere5",
    'dataType': "number"
}
tableTest.create_column(payload)
tableTest.get_table_columns_list()
tableTest.update_column(payload, "HelloThere5")
tableTest.delete_column("HelloThere5")
tableTest.get_table_columns_list()
tableTest.create_column(payload)'''