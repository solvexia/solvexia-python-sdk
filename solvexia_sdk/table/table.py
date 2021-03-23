#!/usr/bin/env python

import requests
import json
import sys
from solvexia_sdk import helper

class table:
    def __init__(self, authorisation, tableId):
        self.authorisation = authorisation
        self.tableId = tableId
        self.baseUrl = "https://app.solvexia.com/api/v1/tables"

    def getTable(self):
        getTableUrl = self.baseUrl + f"/{self.tableId}"
        response = requests.get(getTableUrl, headers=self.authorisation)
        helper.statusCodeCheck(response.status_code, "Error getting table")

        return response.json()

    def createTable(self, name, description):
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        payload = {
            'name': name,
            'description': description
        }
        response = requests.post(self.baseUrl, headers=headers, data=json.dumps(payload))
        helper.statusCodeCheck(response.status_code, "Error creating table")

        return response.json()

    def updateTable(self, name, description):
        updateTableUrl = self.baseUrl + f"/{self.tableId}"
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        payload = {
            'name': name,
            'description': description
        }
        response = requests.post(updateTableUrl, headers=headers, data=json.dumps(payload))
        helper.statusCodeCheck(response.status_code, "Error creating table")

        return response.json()

    def getTableColumns(self):
        getTableColumnsUrl = self.baseUrl + f"/{self.tableId}/columns"
        response = requests.get(getTableColumnsUrl, headers=self.authorisation)
        helper.statusCodeCheck(response.status_code, "Error getting table columns")
        return response.json()

    def createColumn(self, columnInstance):
        createColumnUrl = self.baseUrl + f"/{self.tableId}/columns"
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(createColumnUrl, headers=headers, data=json.dumps(columnInstance))
        helper.statusCodeCheck(response.status_code, "Error creating column")
        return response.json()

    def updateColumn(self, columnInstance, columnName):
        updateColumnUrl = self.baseUrl + f"/{self.tableId}/columns/{columnName}"
        headers = self.authorisation
        headers['Content-Type']= 'application/json'
        response = requests.post(updateColumnUrl, headers=headers, data=json.dumps(columnInstance))
        helper.statusCodeCheck(response.status_code, "Error updating column")
        return response.json()

    def deleteColumn(self, columnName):
        deleteColumnUrl = self.baseUrl + f"/{self.tableId}/columns/{columnName}"
        response = requests.delete(deleteColumnUrl, headers=self.authorisation)
        helper.statusCodeCheck(response.status_code, "Error deleting column")
        return response.json()