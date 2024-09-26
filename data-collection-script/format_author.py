import csv
import re
import sys

csv.field_size_limit(sys.maxsize)
# Input CSV file path and output CSV file path
input_csv_file = "/home/zihan/oscar.py/non_sg_contri_authors.csv"
output_csv_file = "/home/zihan/oscar.py/non_sg_contri_authors_formatted.csv"

# Regular expression pattern to extract values within parentheses
pattern = re.compile(r'<([\w.-]+@[\w.-]+\.[\w]+)>')

# Open the input and output CSV files
with open(input_csv_file, "r", encoding='utf-8') as infile, open(output_csv_file, "w", newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    # Process each row in the original file
    for row in reader:
        # Split the second column into separate entries
        emails = row[1].strip("()").split(", ")
        # Write each entry into the new file
        for email in emails:
            writer.writerow([row[0], email.strip()])

print("CSV file reformatted successfully.")

