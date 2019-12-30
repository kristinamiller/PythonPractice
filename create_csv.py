import os
import csv

file_list = (os.listdir('/Users/kristinamiller/Documents/Freelancing/Genentech/test-folder1577676238'))
output = {}

os.chdir('/Users/kristinamiller/Documents/Freelancing/Genentech/test-folder1577676238')

# print(output)

columns = ['name', 'email', 'boolean', 'squared']

for filename in file_list:
  array = []
  with open(filename, 'r') as rf:
    lines = rf.readlines()
    for column in columns:
      for line in lines:
        if line.find(column) > -1:
          array.append(line[line.find(':') + 2:].strip())
  output[filename] = array

rows = output.values()

# print(rows)

with open('output.csv', 'w') as new_csv:
  csv_writer = csv.writer(new_csv, delimiter=',')
  csv_writer.writerow(columns)

  for row in rows:
    csv_writer.writerow(row)