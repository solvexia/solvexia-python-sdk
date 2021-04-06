#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class dataSteps:
    def __init__(self, stepId):
        self.stepId = stepId

    def get_data_step(self):
        response = api.api_get(f"steps/{self.stepId}")
        api.status_code_check(response, f"Error getting data step with stepId {self.stepId}")
        return response.json()

    def get_data_step_property_list(self):
        response = api.api_get(f"steps/{self.stepId}/properties")
        api.status_code_check(response, f"Error getting data step property list with stepId {self.stepId}")
        return response.json()

    def get_data_step_property_for_data_step(self, propertyId):
        response = api.api_get(f"steps/{self.stepId}/properties/{propertyId}")
        api.status_code_check(response, f"Error getting data step property for a data step with stepId {self.stepId} and propertyId {propertyId}")
        return response.json()

    def update_data_step_property(self, propertyId, dataStepInstance):
        response = api.api_post(f"steps/{self.stepId}/properties/{propertyId}", dataStepInstance)
        api.status_code_check(response, f"Error updating data step property with stepId {self.stepId} and propertyId {propertyId}")
        return response.json()
