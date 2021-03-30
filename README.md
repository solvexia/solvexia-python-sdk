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

### Creating JSON Authentication File

1. Recall your Client Id and Client Secret credentials that you saved previously.
2. Store this information in a JSON file with the structure {'client_id': clientId, 'client_secret': clientSecret}.
3. Save this file in the SOLVEXIA-PYTHON-SDK directory.

### Importing OAuth Function and Generating an Access Token

If the file you are using to call the functions within the SDK is located within the SOLVEXIA-PYTHON-SDK directory,
you can import the api.py as follows to access the OAuth function to generate an access token.

```python
from solvexia_sdk import api
```

We then need to initalise the solvexia_client class within the api python file by indicating which qa enviroment we will be 
using for our calls. We must pass through the qa environment that we will be using to this class so that it can be stored.
E.g. If using the volibear qa environment, we would do the following:

```python
client = api.solvexia_client("volibear.qa")
```

Now to access any of the other functions within the solvexia_client class, we simply do client.[function name]. We will do this
to access the generate access token function within this class. We must pass through the name of the file that contains the
client_id and client_secret.

E.g. 
```python
client.getAccessToken("JSONFileName")
```

After successfully calling this function, we can use all the remaining API calls within the SDK until our access token expires.

### Calling API Functions from the SDK

The available SolveXia API calls are separated into group according to the object they are associated with, e.g. datasteps,
process, file, etc.

The first thing we need to do to access these functions is to import them over to our file so we can access them.
We can do this by following the following general syntax:
```python
from solvexia_sdk.[foldername] import [python_file]
```
E.g. To import the file API calls that are found in the file.py file in the file directory, we do:
```python
from solvexia_sdk.file import file
```
The next step would be to initalise the class within each file by passing through any required parameters.
We do this by doing varName (free to set this to anything you want) = [fileName].[className](anyPossibleParameters)
E.g. To initialise the file class we can see that we need to pass in a fileId
```python
fileClass = file.file("f-5922731")
```
After initalising the class, we can call all the other functions within the class by doing fileClass.[functionName]