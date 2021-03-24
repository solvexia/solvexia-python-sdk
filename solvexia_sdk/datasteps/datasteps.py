#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class datasteps:
    def __init__(self, stepId):
        self.stepId = stepId
        self.baseUrl = "https:///app.solvexia.com/api/v1/steps/"

    def getDataStep(self):
        response = api.apiGet(f"steps/{self.stepId}")
        api.statusCodeCheck(response, "Error getting data step")
        return response.json()

    def getDataStepProperties(self):
        response = api.apiGet(f"steps/{self.stepId}/properties")
        api.statusCodeCheck(response, "Error getting data step properties")
        return response.json()

    def getDataStepPropertyForDataStep(self, propertyId):
        response = api.apiGet(f"steps/{self.stepId}/properties/{propertyId}")
        api.statusCodeCheck(response, "Error getting data step property for a data step")
        return response.json()

    def updateDataStepProperty(self, propertyId, dataStepInstance):
        response = api.apiPost(f"steps/{self.stepId}/properties/{proertyId}", dataStepInstance)
        api.statusCodeCheck(response, "Error updating data step property")
        return response.json()
