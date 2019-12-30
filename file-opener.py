import os

file_list = (os.listdir('/Users/kristinamiller/Documents/Freelancing/Genentech/test-folder1577676238'))
files = {}
# print(file_list)
num_files = len(file_list)
output = []

os.chdir('/Users/kristinamiller/Documents/Freelancing/Genentech/test-folder1577676238')

columns = ['name', 'email', 'boolean', 'squared']
array = []
for filename in file_list:
  with open(filename, 'r') as rf:
    lines = rf.readlines()
    for column in columns:
      for line in lines:
        if line.find(column) > -1:
          output.append(line[line.find(':') + 2:].strip())

  
  
# output.append(array)  

print(output)



# with open('test.txt', 'r') as rf:
#   with open('test_copy.txt', 'w') as wf:
#     for line in rf:
#       if line.find("all") > -1:
#         print(line.strip())

