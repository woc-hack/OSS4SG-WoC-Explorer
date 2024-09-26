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
            for commit in Project(str(match)).commit_shas:
                print(commit)
                b=commit
                b=b.replace("b'","").replace("'","")
                result.append([formatted,b])
                print([match,b])

with open('/home/zihan/oscar.py/non_sg_contri_repo_commit.csv', "w") as f:
   writer = csv.writer(f)
   header_line = [ 'projects','commit']
   writer.writerow(header_line)
   for row in result:
        writer.writerow(row)
