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