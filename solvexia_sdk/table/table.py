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
        api.statusCodeCheck(response, "Error getting table")
        print(response.json())
        return response.json()

    def createTable(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.apiPost("tables", payload)
        api.statusCodeCheck(response, "Error creating table")
        print(response.json())
        return response.json()

    def updateTable(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.apiPost(f"tables/{self.tableId}", payload)
        api.statusCodeCheck(response, "Error updating table")
        print(response.json())
        return response.json()

    def getTableColumns(self):
        response = api.apiGet(f"tables/{self.tableId}/columns")
        api.statusCodeCheck(response, "Error getting table columns")
        print(response.json())
        return response.json()

    def createColumn(self, columnInstance):
        response = api.apiPost(f"tables/{self.tableId}/columns", columnInstance)
        api.statusCodeCheck(response, "Error creating column")
        print(response.json())
        return response.json()

    def updateColumn(self, columnInstance, columnName):
        response = api.apiPost(f"tables/{self.tableId}/columns/{columnName}", columnInstance)
        api.statusCodeCheck(response, "Error updating column")
        print(response.json())
        return response.json()

    def deleteColumn(self, columnName):
        deleteColumnUrl = api.baseUrl + f"tables/{self.tableId}/columns/{columnName}"
        response = requests.delete(deleteColumnUrl, headers=api.access_token)
        api.statusCodeCheck(response, "Error deleting column")
        return 