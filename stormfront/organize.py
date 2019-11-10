import os

metadata = open("annotations_metadata.csv")
output = open("test_set.csv","w")

testfiles = os.listdir("sampled_test")

for line in metadata.readlines()[1:]:
  fileno, _, _, _, label = line.strip().split(",")
  if "{}.txt".format(fileno) not in testfiles:
    continue
  
  with open("./all_files/{}.txt".format(fileno)) as content_file:
    content = content_file.readline()
  #print(fileno, label, content)
  output.write('{},{},"{}"\n'.format(fileno, label, content))

metadata.close()
output.close()