#!/usr/bin/env python

from solvexia_sdk import api

client = api.solvexia_client("CDA77AD1-168D-EB11-82D5-000D3AD127EB", "fsORNx&Y61eAn3PpE2%", "volibear.qa")
client.getAccessToken()