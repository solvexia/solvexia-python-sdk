#!/usr/bin/env python

import requests
import json
import sys

def statusCodeCheck(statusCode, errorMessage):
    if statusCode != 200:
        print(errorMessage)
        sys.exit()