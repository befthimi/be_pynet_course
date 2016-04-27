#!/usr/bin/env python
# Class 1, Exercise 7
"""
Read in two files. myList.yml & myList.json.
Pretty prints the contents of these two files.
"""
import pprint
import json
import yaml

print "\n----------------------"
print "Pretty Print YAML file"
print "----------------------"
with open("myList.yml") as f:
    myList = yaml.load(f)
    pprint.pprint(myList)
f.close()

print "\n----------------------"
print "Pretty Print JSON file"
print "----------------------"
with open("myList.json") as f:
    myList = json.load(f)
    pprint.pprint(myList)

f.close()

print "\n"
