from solvexia_sdk import api
from solvexia_sdk.file import file
from solvexia_sdk.process import process
from solvexia_sdk.processrun import processrun
from solvexia_sdk.datasteps import datasteps
from solvexia_sdk.table import table
from hashlib import md5
import os


def main():

    client = api.solvexiaClient("auth.json")
    client.get_access_token()

    processTest = process.process("p-4631")
    final_file_list = processTest.get_process_file_list()
    process_list = processTest.get_process_data_step_list()
    print(final_file_list)
    print(process_list)

    dataStepsTest = datasteps.dataSteps("ds-6061")
    test_list = dataStepsTest.get_data_step_file_list()
        
    print(test_list)

    fileTest = file.file("f-7400")
    print("Calculating original file's MD5")
    original_md5 = calculate_md5("test14.xlsx")
    print("Uploading chunks")
    fileTest.upload_file_by_chunks("test14.xlsx", 4000000)

    print("Finished uploading. Now downloading")
    response = fileTest.download_file()
    download_file = "downtest14.xlsx"
    with open(download_file, "wb") as f:
        f.write(response.content)
    print("Calculating returned file's MD5")
    returned_md5 = calculate_md5(download_file)
    
    if original_md5 == returned_md5:
        print("MD5s match")
    else:
        print("MD5s do not match")

    os.remove(download_file)


def calculate_md5(filename):
    with open(filename, "rb") as open_file:
        data = open_file.read()
        created_md5 = md5(data).hexdigest()
    return created_md5

if __name__ == "__main__":
    main()





# fileTest = file.file("f-5940022")
# fileTest.get_file_metadata() 
# fileTest.upload_file("Upload-test.csv")
# fileTest.update_file_metadata("Thisisatest.csv")
# fileTest.download_file()
# fileTest.start_upload_session()
# fileTest.upload_chunk("CollectedClientResponse.csv", 100)
# fileTest.commit_upload()
# fileTest.upload_file_by_chunks("CollectedClientResponse.csv", 100)

# processRunTest = processrun.processRuns("pr-5916704")
# processRunTest.get_process_run()
# processRunTest.get_process_run_status()
# processRunTest.get_process_run_data_steps_list()
# processRunTest.start_process_run()
# processRunTest.cancel_process_run()


# processTest = process.process("p-5854642")
# processTest.get_process_list()
# processTest.get_process()
# processTest.create_process_run("hello bob")
# processTest.get_process_run_list()
# processTest.get_process_data_step_list()


# dataStepsTest = datasteps.dataSteps("ds-5854643")
# dataStepsTest.get_data_step()
# dataStepsTest.get_data_step_property_list()
# dataStepsTest.get_data_step_property_for_data_step("dsprop-1844675")
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
# dataStepsTest.update_data_step_property("dsprop-1844675", payload)
# dataStepsTest.get_data_step_property_for_data_step("dsprop-1844675")


# tableTest = table.table("mt-5922660")
# tableTest.get_table()
# tableTest.create_table("newName12", "newDescription")
# tableTest.update_table("newName14", "newDescription")
# tableTest.get_table_columns_list()
# payload = {
#     'name': "HelloThere5",
#     'dataType': "number"
# }
# tableTest.create_column(payload)
# tableTest.get_table_columns_list()
# tableTest.update_column(payload, "HelloThere5")
# tableTest.delete_column("HelloThere5")
# tableTest.get_table_columns_list()
# tableTest.create_column(payload)

# userTest = user.user("u-1225")
# userTest.get_user_list()
# userTest.get_user()
# userTest.get_permissions()
# userTest.add_permission("p-4250", "reader")
# userTest.update_permission("p-4250", "editor")
# userTest.delete_permission("p-4250")
# userTest.create_user("samplingsolvixatest@gmail.com", "Jet", "Bing", "SuperStrong123", "Subscriber", "(UTC-03:00) Greenland")
# userTest.update_user("Josh", None, None, "Active", None, None, None, None, None, None, None, None)

# userGroupTest = usergroup.userGroup("ug-1248")
# userGroupTest.get_usergroup()
# userGroupTest.get_usergroup_list()
# userGroupTest.get_users()
# userGroupTest.add_user("u-1225")
# userGroupTest.remove_user("u-1225")
# userGroupTest.get_permissions()
# userGroupTest.delete_permission("p-1217")
# userGroupTest.add_permission("p-1217", "reader")
# userGroupTest.update_permission("p-1217", "editor")