#!/usr/bin/env python

import requests
import json
import sys

class table:
    def __init__(self, authorisation, tableId):
        self.authorisation = authorisation
        self.tableId = tableId
        self.baseUrl = "https://app.solvexia.com/api/v1/tables"

    def getTable(self):
        getTableUrl = self.baseUrl + f"/{self.tableId}"
        response = requests.get(getTableUrl, headers=self.authorisation)

        if response.status_code() != 200:
            print("Error getting table")
            sys.exit()

        return response.json()

    def createTable(self, name, description):
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        payload = {
            'name': name,
            'description': description
        }
        response = requests.post(self.baseUrl, headers=headers, data=json.dumps(payload))
        if response.status_code() != 200:
            print("Error creating table")
            sys.exit()

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
        if response.status_code() != 200:
            print("Error creating table")
            sys.exit()

        return response.json()

    def getTableColumns(self):
        getTableColumnsUrl = self.baseUrl + f"/{self.tableId}/columns"
        response = requests.get(getTableColumnsUrl, headers=self.authorisation)
        if response.status_code() != 200:
            print("Error getting table columns")
            sys.exit()
        return response.json()

    def createColumn(self, columnInstance):
        createColumnUrl = self.baseUrl + f"/{self.tableId}/columns"
        headers = self.authorisation
        headers['Content-Type'] = 'application/json'
        response = requests.post(createColumnUrl, headers=headers, data=json.dumps(columnInstance))
        if response.status_code() != 200:
            print("Error creating column")
            sys.exit()
        return response.json()

    def updateColumn(self, columnInstance, columnName):
        updateColumnUrl = self.baseUrl + f"/{self.tableId}/columns/{columnName}"
        headers = self.authorisation
        headers['Content-Type']= 'application/json'
        response = requests.post(updateColumnUrl, headers=headers, data=json.dumps(columnInstance))
        if response.status_code() != 200:
            print("Error updating column")
            sys.exit()
        return response.json()

    def deleteColumn(self, columnName):
        deleteColumnUrl = self.baseUrl + f"/{self.tableId}/columns/{columnName}"
        response = requests.delete(deleteColumnUrl, headers=self.authorisation)
        if response.status_code() != 200:
            print("Error deleting column")
            sys.exit()
        return response.json()