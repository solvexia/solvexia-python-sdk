#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class table:
    def __init__(self, tableId):
        self.tableId = tableId

    def get_table(self):
        response = api.api_get(f"tables/{self.tableId}")
        api.status_code_check(response, f"Error getting table with tableId {self.tableId}")
        return response.json()

    def create_table(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.api_post("tables", payload)
        api.status_code_check(response, f"Error creating table with tableId {self.tableId}")
        return response.json()

    def update_table(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.api_post(f"tables/{self.tableId}", payload)
        api.status_code_check(response, f"Error updating table with tableId {self.tableId}")
        return response.json()

    def get_table_columns_list(self):
        response = api.api_get(f"tables/{self.tableId}/columns")
        api.status_code_check(response, f"Error getting table columns with tableId {self.tableId}")
        return response.json()

    def create_column(self, columnInstance):
        response = api.api_post(f"tables/{self.tableId}/columns", columnInstance)
        api.status_code_check(response, f"Error creating column for table with tableId {self.tableId}")
        return response.json()

    def update_column(self, columnInstance, columnName):
        response = api.api_post(f"tables/{self.tableId}/columns/{columnName}", columnInstance)
        api.status_code_check(response, f"Error updating column with columnName {columnName} for table with tableId {self.tableId}")
        return response.json()

    def delete_column(self, columnName):
        deleteColumnUrl = api.baseUrl + f"tables/{self.tableId}/columns/{columnName}"
        response = requests.delete(deleteColumnUrl, headers=api.accessToken)
        api.status_code_check(response, f"Error deleting column with columnName {columnName} for table with tableId {self.tableId}")