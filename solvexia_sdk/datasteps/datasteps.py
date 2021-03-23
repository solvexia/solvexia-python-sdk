#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import helper

class datasteps:
    def __init__(self, authorisation, stepId):
        self.authorisation = authorisation
        self.stepId = stepId
        self.baseUrl = "https:///app.solvexia.com/api/v1/steps/"

    def getDataStep(self):
        getDataStepUrl = self.baseurl + self.stepId
        response = requests.get(getDataStepUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting data step")
        return response.json()

    def getDataStepProperties(self):
        getDataStepPropertiesUrl = self.baseurl + f"{self.stepId}/properties"
        response = requests.get(getDataStepPropertiesUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting data step properties")
        return response.json()

    def getDataStepPropertyForDataStep(self, propertyId):
        getDataStepPropertyForDataStepUrl = self.baseurl + f"{self.stepId}/properties/{propertyId}"
        response = requests.get(getDataStepPropertyForDataStepUrl, headers=self.authorisation)
        helper.statusCodeCheck(response, "Error getting data step property for a data step")
        return response.json()

    def updateDataStepProperty(self, propertyId, dataStepInstance):
        updateDataStepPropertyUrl = self.baseurl + f"{self.stepId}/properties/{propertyId}"
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(updateDataStepPropertyUrl, data=json.dumps(dataStepInstance), headers=headers)
        helper.statusCodeCheck(response, "Error updating data step property")
        return response.json()
        