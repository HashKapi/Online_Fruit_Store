#! /usr/bin/env python3
import os
import requests

url = 'http://34.136.69.242/upload/'

img_path = os.path.dirname(__file__) + '/supplier-data/images'

for file in os.listdir(img_path):
    f = os.path.join(img_path, file)
    name, ext = os.path.splitext(file)
    if ext == '.jpeg':
        with open(f, 'rb') as ima:
            r = requests.post(url, files={'file': ima})
