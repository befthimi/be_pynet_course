#!/usr/bin/env python
"""
Exercise 4c prints the MIB2 SysName and sysDescr of the nominated device (tuple)
"""
from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
PYNET_RTR1_SNMP_PORT = 7961
PYNET_RTR2_SNMP_PORT = 8061
IP_ADDR = '50.76.53.27'

RTR1 = (IP_ADDR, COMMUNITY_STRING, PYNET_RTR1_SNMP_PORT)
RTR2 = (IP_ADDR, COMMUNITY_STRING, PYNET_RTR2_SNMP_PORT)
device_list = [RTR1, RTR2]

OID_sysDescr = '1.3.6.1.2.1.1.1.0'
OID_SysName = '1.3.6.1.2.1.1.5.0'

for device in device_list:
    snmp_data = snmp_get_oid(device, OID_SysName)
    textoutput = snmp_extract(snmp_data)
    print "- " * 18
    print "System Name: %s\n" % textoutput
    snmp_data = snmp_get_oid(device, OID_sysDescr)
    textoutput = snmp_extract(snmp_data)
    print "System Description: %s\n" % textoutput
