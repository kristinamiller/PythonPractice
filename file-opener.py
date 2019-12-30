

with open('test.txt', 'r') as rf:
  with open('test_copy.txt', 'w') as wf:
    for line in rf:
      if line.find("all") > -1:
        print(line.strip())

