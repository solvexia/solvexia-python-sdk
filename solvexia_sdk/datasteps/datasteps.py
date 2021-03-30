#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class datasteps:
    def __init__(self, stepId):
        self.stepId = stepId

    def getDataStep(self):
        response = api.apiGet(f"steps/{self.stepId}")
        api.statusCodeCheck(response, f"Error getting data step with stepId {self.stepId}")
        return response.json()

    def getDataStepPropertyList(self):
        response = api.apiGet(f"steps/{self.stepId}/properties")
        api.statusCodeCheck(response, f"Error getting data step property list with stepId {self.stepId}")
        return response.json()

    def getDataStepPropertyForDataStep(self, propertyId):
        response = api.apiGet(f"steps/{self.stepId}/properties/{propertyId}")
        api.statusCodeCheck(response, f"Error getting data step property for a data step with stepId {self.stepId} and propertyId {propertyId}")
        return response.json()

    def updateDataStepProperty(self, propertyId, dataStepInstance):
        response = api.apiPost(f"steps/{self.stepId}/properties/{propertyId}", dataStepInstance)
        api.statusCodeCheck(response, f"Error updating data step property with stepId {self.stepId} and propertyId {propertyId}")
        return response.json()
