#!/usr/bin/env python
"""
Class 1, Exercise 10
Find the crypto maps that are not using AES (based-on the transform set name).
Print these entries and their corresponding transform set name.
"""
from ciscoconfparse import CiscoConfParse

cisco_config = CiscoConfParse("cisco_ipsec.txt")

print """\nThis script lists the crypto maps that are not using AES in the
transform set and the transform set name"""
print"-" * 114

no_AES_crymaps = cisco_config.find_objects_wo_child(r'crypto map CRYPTO', r'AES')
for obj in no_AES_crymaps:
    print "Crypto-map name: %s" % obj.text
    for child in obj.children:
        if "transform-set" in child.text:
            mystring = child.text
            mystringlist = mystring.split()
            count = 0
            for i in mystringlist:
                if mystringlist[count] == "transform-set":
                    count = count + 1
                    print "Transform-set name is: %s\n" % mystringlist[count]
                    exit()
                else:
                    count = count + 1

print"-" * 114
