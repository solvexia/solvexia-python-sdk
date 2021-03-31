# SolveXia Process Automation SDK for Python

SolveXia Python SDK exists to help create faster and easier integration with SolveXia APIs. 
The package is currently under development and will be pushed to the main Python package repository as soon as the first stable version is achieved.

## Getting started

Any application that is intended to access SolveXia Public API must have authorization credentials that identify the application to SolveXia authorization server.

### Create authorization credentials for you app

1. Navigate to SolveXia API portal from the user dropdown menu.
2. Click "Create new application".
3. Specify the name and callback URL. Click "Create application".
4. If the creation is successful you will see Client Id and Client Secret credentials generated.
5. Copy credentials and store them safely. You will not be able to see Client Secret again unless you generate a new one.

## Install package

```shell
pip install git+https://github.com/solvexia/solvexia-python-sdk#egg=solvexia_api
```

If you keep to use the latest or any other specific version of the package checkout this repo desired version and run

```shell
python setup.py install
```

### Install SDK from GitHub
An alternative way to install the SDK is to download all the necessary files as a zip from GitHub.

### Creating JSON Authentication File

1. Recall your Client Id and Client Secret credentials that you saved previously.
2. Store this information in a JSON file with the structure:
```python
{'client_id': clientId, 'client_secret': clientSecret}.
```
3. Save this file in the root directory (directory that contains the solvexia_sdk folder).

### Importing OAuth Function and Generating an Access Token
SolveXia uses OAuth2.0 as a secure method to generate access tokens for clients so that they can access and use SolveXia's
API calls. Therefore, before we can use any of the functions within the SDK, we must first obtain our access token using
our client_id and client_secret. Using the JSON file we created earlier, we can import the api.py as follows to access 
the solvexia_client class which contains the access token generation function.

```python
from solvexia_sdk import api
```

We then need to initalise the solvexia_client class by indicating and passing through the qa enviroment we will be using for 
our calls. This environment should match the one that you used to create your client_id and client_secret.
E.g. If I generated my client_id and client_secret within the volibear qa environment, I would do the following class initialisation:

```python
client = api.solvexia_client("volibear.qa")
```

Note: client is just a variable name that represents the initialised class and can be set to anything you desire.

Once our solvexia_client class has been initialised, we can now generate our access token. This is performed through the 
getAccessToken function within the solvexia_client class and must have a JSON file containing the client_id and client_secret
passed as an argument.

E.g. Calling the getAccessToken function within the solvexia_client class
```python
client.getAccessToken("JSONFileName")
```

If no errors are raised, we have now successfully generated our access token and we are free to use all the other functions and
API calls within this SDK until the token expires.

### Importing API SDK Files

Within this SDK, SolveXia's API calls are separated into groups based on the type of object they operate on, e.g. datasteps,
process, file, etc.

The first thing we need to do to access these functions is to import them over to our file.
We can do this by following the general syntax:
```python
from solvexia_sdk.foldername import python_file
```
E.g. To import the file API calls and class that are found in the file.py file in the file directory, we do:
```python
from solvexia_sdk.file import file
```

### Initialising Classes

After importing an API SDK file, we must initialise the class specified within that particular file before we can access the
class functions. Make sure to take note of what variable we need to pass in during class initialisation by looking at the 
arguments (besides self) within the class __init__ function.
To do this, we can follow the following general syntax:
```python
    classNameVar = fileName.className(anyArgs)
```
E.g. To initialise the file class within file.py, we need to pass in a fileId.
```python
fileClass = file.file("f-5922731")
```

### Calling the Functions within a Class
Now that the class has been initialised, we are free to access any of the functions within that class. The generic
code to do this is as follows:
```python
    retObj = classNameVar.classFunction(anyArgs)
```
Since most of the functions within this SDK will return a JSON object, generally we want to store that in a variable
so that we can access this information (retObj).
E.g. Calling the getFileMetadata function with an initialised file class called fileClass and storing the response in a 
variable called response.
```python
    response = fileClass.getFileMetadata()
```

Reminder: Ensure that for any of the object classes, we must always initialise the class first before we can call 
any functions from within the class.

### Return Value of API Functions
A majority of the API call functions within this SDK will return a JSON object specific to the object. These JSON objects
and their format are explained in depth in SolveXia's API docs.
An alternative to see the structure of the return JSON object is to print the JSON object that is returned by the function
to stdout.

### Additional Arguments for Functions
Some API function calls within this SDK have additional arguments that must be passed through. In most cases, these are 
either additional ids or an object instance.

### Structure of Object Instance Docs
[File Objects](https://github.com/solvexia/solvexia-api-docs/blob/master/file/file_schemas.md/#upload-session)
[Process Run Objects](https://github.com/solvexia/solvexia-api-docs/blob/master/process_runs/process_runs_schemas.md)
[Process Objects](https://github.com/solvexia/solvexia-api-docs/blob/master/processes/schemas.md)
[Datasteps Objects](https://github.com/solvexia/solvexia-api-docs/blob/master/steps/datastep_schemas.md)
[Table Objects](https://github.com/solvexia/solvexia-api-docs/blob/master/tables/tables_schemas.md)