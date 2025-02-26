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
