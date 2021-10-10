#! /usr/bin/env python3

import os
import requests

url = 'http://34.136.69.242/fruits/'
path = os.path.dirname(__file__) + '/supplier-data/descriptions/'
file_data = []
for file in os.listdir(path):
    act_path = os.path.join(path, file)
    with open(act_path) as f:
        lines = f.readlines()
        file_data = {'name': lines[0].strip('\n'),
                     'weight': int(lines[1].strip('lbs')),
                     'description': ' '.join(lines[2:]).replace('\n', ''),
                     'image_name': file
                     }
        print(file_data)
        r = requests.post(url, json=file_data)
        print("STATUS CODE:", r.status_code)
