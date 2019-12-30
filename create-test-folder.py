import os


cur_time = os.stat('create-test-folder.py').st_atime
new_folder = 'test-folder' + str(round(cur_time))

os.chdir('/Users/kristinamiller/Documents/Freelancing/Genentech')
os.mkdir(new_folder)
os.chdir(f'/Users/kristinamiller/Documents/Freelancing/Genentech/{new_folder}')

array = ['esther', 'liz', 'lynette', 'heidi', 'kristina', 'edmund', 'miranda', 'tracy', 'donna', 'katherine', 'joel', 'alaina']

for n in range(1,11):
  with open(f'new_file{n}.txt', 'w') as wf:
    wf.write(f'this is new test file number #{n}\n')
    wf.write(f'squared: {n * n}\n')
    wf.write(f'boolean: {n == 3}\n')
    wf.write(f'name: {array[n]}\n')