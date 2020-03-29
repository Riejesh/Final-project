#!/usr/bin/env python3

import requests
import json
import os

os.chdir("/data/feedback/")
for file in os.listdir():
    with open(file, "r") as f:
        feedback = {}
        colume = ["title", "name", "date", "feedback"]
        n = 0
        for line in f:
            feedback[colume[n]] = line.rstrip("\n")
            n += 1
        #json_feedback = json.dumps(feedback)
        #print(json_feedback)
        response = requests.post("http://35.188.2.103/feedback/", json=feedback)
        print(response.status_code)

