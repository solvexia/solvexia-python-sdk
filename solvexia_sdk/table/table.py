#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class table:
    def __init__(self, tableId):
        self.tableId = tableId

    def getTable(self):
        response = api.apiGet(f"tables/{self.tableId}")
        api.statusCodeCheck(response, f"Error getting table with tableId {self.tableId}")
        print(response.json())
        return response.json()

    def createTable(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.apiPost("tables", payload)
        api.statusCodeCheck(response, f"Error creating table with tableId {self.tableId}")
        print(response.json())
        return response.json()

    def updateTable(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.apiPost(f"tables/{self.tableId}", payload)
        api.statusCodeCheck(response, f"Error updating table with tableId {self.tableId}")
        print(response.json())
        return response.json()

    def getTableColumnsList(self):
        response = api.apiGet(f"tables/{self.tableId}/columns")
        api.statusCodeCheck(response, f"Error getting table columns with tableId {self.tableId}")
        print(response.json())
        return response.json()

    def createColumn(self, columnInstance):
        response = api.apiPost(f"tables/{self.tableId}/columns", columnInstance)
        api.statusCodeCheck(response, f"Error creating column for table with tableId {self.tableId}")
        print(response.json())
        return response.json()

    def updateColumn(self, columnInstance, columnName):
        response = api.apiPost(f"tables/{self.tableId}/columns/{columnName}", columnInstance)
        api.statusCodeCheck(response, f"Error updating column with columnName {columnName} for table with tableId {self.tableId}")
        print(response.json())
        return response.json()

    def deleteColumn(self, columnName):
        deleteColumnUrl = api.baseUrl + f"tables/{self.tableId}/columns/{columnName}"
        response = requests.delete(deleteColumnUrl, headers=api.access_token)
        api.statusCodeCheck(response, f"Error deleting column with columnName {columnName} for table with tableId {self.tableId}")
        return 