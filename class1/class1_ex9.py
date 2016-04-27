#!/usr/bin/env python
"""
# Class 1, Exercise 9
# Find all of the crypto map entries that are using PFS group2
"""
from ciscoconfparse import CiscoConfParse

num_cryptomaps_w_PFS = 0
cisco_config = CiscoConfParse("cisco_ipsec.txt")

list_crypto_maps = cisco_config.find_objects(r"^crypto map CRYPTO")

print "\n This script lists the crypto maps that are using PFS group2"
print"-" * 50
for PFSG2 in list_crypto_maps:
    if PFSG2.re_search_children(r"pfs group2"):
        print PFSG2.text
        num_cryptomaps_w_PFS += 1
print"-"  * 50
print "Found a total of %d crypto maps with PFS group2.\n" % num_cryptomaps_w_PFS

