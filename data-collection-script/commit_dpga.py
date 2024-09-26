#！/usr/bin/env python


import csv
import re
from oscar import Commit
# pattern = re.compile(r'(\w+) <([\w.-]+@[\w.-]+\.[\w]+)>')
result=[]

with open("/home/zihan/oscar.py/Cdpga_user_commit.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    headers=next(reader)
    for row in reader:
        match = (row[1])
        user = (row[0])
        if match:
            project=str(Commit(str(match)).project_names)
            b=project.replace("b'","").replace("'","")
            attribute=Commit(str(match)).attributes
            print([user,match,b]+attribute)
            result.append([user,match,b]+attribute)

with open('/home/zihan/oscar.py/dpga_user_commit.csv', "w") as f:
   writer = csv.writer(f)
   header_line = ['user','commit','projects','time','tz','author', 'tree', 'parent']
   writer.writerow(header_line)
   for row in result:
        writer.writerow(row)
