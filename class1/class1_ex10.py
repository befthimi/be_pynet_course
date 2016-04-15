# Class 1, Exercise 10
# Find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
# There are two methods of computing the result. One of which is commented out.
#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

#num_cryptomaps_wo_AES = 0
cisco_config = CiscoConfParse ("cisco_ipsec.txt")

#list_crypto_maps = cisco_config.find_objects(r"^crypto map CRYPTO")

print "\nThis script lists the crypto maps that are not using AES in the transform set"
print"----------------------------------------------------------------------------------"
#for crymap in list_crypto_maps:
#    if not crymap.re_search_children(r"AES"):
#        print crymap.text
#        num_cryptomaps_wo_AES += 1
#print"-----------------------------------------------------------------"
#print "Found a total of %d crypto maps without AES in transform set.\n" % num_cryptomaps_wo_AES



no_AES_crymaps = cisco_config.find_objects_wo_child(r'crypto map CRYPTO', r'AES')
for obj in no_AES_crymaps:
    print obj.text

print"---------------------------------------------------------------------------------"
