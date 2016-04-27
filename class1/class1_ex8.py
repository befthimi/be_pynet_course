#!/usr/bin/env python
# Class 1, Exercise 8
"""
Finds all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and
for each crypto map entry prints out its children.
"""
from ciscoconfparse import CiscoConfParse

num_cryptomaps = 0
cisco_config = CiscoConfParse("cisco_ipsec.txt")

#print cisco_config
print "===========\n"
for obj in cisco_config.find_objects(r"^crypto map CRYPTO"):
    print obj.text
    num_cryptomaps += 1
    for child in obj.children:
        print child.text

print "\nFound %d crypto maps." % num_cryptomaps

