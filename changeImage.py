#! /usr/bin/env python3
from PIL import Image
import os


img_path = '~/supplier-data/images'

for file in os.listdir(img_path):
    f = os.path.join(img_path,file)
    name, ext = os.path.splitext(file)

    if name != '.DS_Store':
        new_format = os.path.join(img_path,name+'.jpeg')

        try:
            with Image.open(f) as im:
                im.convert('RGB').resize((600,400)).save(new_format)
        except OSError:
            print('Cannot convert',file)