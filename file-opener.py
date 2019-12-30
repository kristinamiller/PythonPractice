import os

file_list = (os.listdir('/Users/kristinamiller/Documents/Freelancing/Genentech/test-folder1577676238'))
files = {}
print(file_list)
num_files = len(file_list)

os.chdir('/Users/kristinamiller/Documents/Freelancing/Genentech/test-folder1577676238')

for filename in file_list:
  with open(filename, 'r') as rf:
    for line in rf:
      if line.find('name') > -1:
        print(line[line.find(':') + 2:].strip())




# with open('test.txt', 'r') as rf:
#   with open('test_copy.txt', 'w') as wf:
#     for line in rf:
#       if line.find("all") > -1:
#         print(line.strip())

