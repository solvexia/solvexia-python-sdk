#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import api

class table:
    def __init__(self, tableId):
        self.tableId = tableId
        self.baseUrl = "https://app.solvexia.com/api/v1/tables"

    def getTable(self):
        getTableUrl = self.baseUrl + f"/{self.tableId}"
        response = requests.get(getTableUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting table")

        return response.json()

    def createTable(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.apiPost("tables", payload)
        api.statusCodeCheck(response, "Error creating table")

        return response.json()

    def updateTable(self, name, description):
        payload = {
            'name': name,
            'description': description
        }
        response = api.apiPost(f"tables/{self.tableId}", payload)
        api.statusCodeCheck(response, "Error creating table")

        return response.json()

    def getTableColumns(self):
        getTableColumnsUrl = self.baseUrl + f"/{self.tableId}/columns"
        response = requests.get(getTableColumnsUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error getting table columns")
        return response.json()

    def createColumn(self, columnInstance):
        response = api.apiPost(f"tables/{self.tableId}/columns", columnInstance)
        api.statusCodeCheck(response, "Error creating column")
        return response.json()

    def updateColumn(self, columnInstance, columnName):
        response = api.apiPost(f"tables/{self.tableId}/columns/{columnName}", columnInstance)
        api.statusCodeCheck(response, "Error updating column")
        return response.json()

    def deleteColumn(self, columnName):
        deleteColumnUrl = self.baseUrl + f"/{self.tableId}/columns/{columnName}"
        response = requests.delete(deleteColumnUrl, headers=self.authorisation)
        api.statusCodeCheck(response, "Error deleting column")
        return response.json()