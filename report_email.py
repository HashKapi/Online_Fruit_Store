#! /usr/bin/env python3

import os
import datetime
import reports

path = os.path.dirname(__file__) + '/supplier-data/descriptions'
fru_info = ""
for file in os.listdir(path):
    lines = file.readlines()
    fru_info += "name:" + lines[0].strip('\n') +"\n"+"weight:"+lines[1].strip('\n')+"\n[blank line]\n"

if __name__ == '__main__':
    reports.generate_report('/tmp/processed.pdf', 'Processed Update on ' + str(datetime.date.today()), fru_info)

