# Class 1, Exercise 7
# reads in two files: myList.yml & myList.json
# pretty prints the contents of these two files
#!/usr/bin/env python


import yaml
import json
import pprint

print "\n----------------------"
print "Pretty Print YAML file"
print "----------------------"
with open ("myList.yml") as f:
    myList = yaml.load(f)
    pprint.pprint(myList)
f.close()

print "\n----------------------"
print "Pretty Print JSON file"
print "----------------------"
with open ("myList.json") as f:
    myList = json.load(f)
    pprint.pprint(myList)

f.close()

print "\n"
