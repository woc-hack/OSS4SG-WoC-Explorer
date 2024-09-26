#！/usr/bin/env python


import csv
import re
from oscar import Author, Commit, Project
pattern = re.compile(r'(\w+) <([\w.-]+@[\w.-]+\.[\w]+)>')
result=[]

with open("/home/zihan/oscar.py/non_sg_contri_authors_formatted.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    headers=next(reader)
    for row in reader:
        match = pattern.search(row[1])
        if match:
            name, email = match.groups()
            formatted = f'{name} <{email}>'
            for commit in Author(str(formatted)).commit_shas:
                b=str(Commit(commit))
                b=b.replace("b'","").replace("'","")
		# b =Commit(commit).attributes 
                # a =Commit(commit).project_names
                # c= Commit(commit).reporoot
                result.append([formatted,b])

with open('/home/zihan/oscar.py/non_sg_contri_user_commit.csv', "w") as f:
   writer = csv.writer(f)
   header_line = ['user','commit']
   writer.writerow(header_line)
   for row in result:
        writer.writerow(row)
