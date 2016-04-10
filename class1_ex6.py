# Class 1, Exercise 6
# output is two files: myList.yml & myList.json
# 
import yaml
import json
import pprint

myList = []

# create a list beginning with 10 nums.
for i in range (10):
 myList.append(i)

# Add a dict with 3 Australia states and with abbreviations
myList.append({'NSW': 'New South Wales', 'VIC': 'Victoria', 'TAS': 'Tasmansia'})

print "\nHere is my list:"
print myList

print "print in expanded YAML format to myList.yml\n"
with open ("myList.yml" ,'w') as f:
    f.write(yaml.dump(myList, default_flow_style=False))
f.close()

print "print in JSON format to myList.json\n"
with open ("myList.json", 'w') as f:
    json.dump(myList, f)
f.close()

