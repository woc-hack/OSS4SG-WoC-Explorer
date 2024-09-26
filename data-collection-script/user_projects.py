#！/usr/bin/env python


import csv
import re
from oscar import Author, Commit, Project
pattern = re.compile(r'(\w+) <([\w.-]+@[\w.-]+\.[\w]+)>')
result=[]

with open("/home/zihan/oscar.py/new_ran_100_contri_format.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    headers=next(reader)
    for row in reader:
        match = pattern.search(row[1])
        if match:
            name, email = match.groups()
            formatted = f'{name} <{email}>'
            b=str(Author(str(formatted)).project_names)
            b=b.replace("b'","").replace("'","")
            result.append([formatted,b])

with open('/home/zihan/oscar.py/new_ran_100_contri_projects.csv', "w") as f:
   writer = csv.writer(f)
   header_line = ['user', 'projects']
   writer.writerow(header_line)
   for row in result:
        writer.writerow(row)
