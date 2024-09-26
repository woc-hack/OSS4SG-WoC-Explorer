#?~A/usr/bin/env python
import csv
import re
from oscar import Author, Commit, Project
pattern = re.compile(r'(\w+) <([\w.-]+@[\w.-]+\.[\w]+)>')
result=[]

with open("/home/zihan/oscar.py/non_sg_contri_repo.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers=next(reader)
    for row in reader:
        match = row[0]
        if match:
            match_str = "'" + str(match) + "'"
            #print(str(match))
            b=str(Project(str(match)).author_names)
            #print(b)
            b=b.replace("b'","").replace("'","")
            result.append([match,b])

with open('/home/zihan/oscar.py/non_sg_contri_authors.csv', "w") as f:
   writer = csv.writer(f)
   header_line = [ 'projects','user']
   writer.writerow(header_line)
   for row in result:
        writer.writerow(row)
