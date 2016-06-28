#!/usr/bin/env python
"""
    Exercose 1 class 10.
"""
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

def getdevice(ip_address, username, password):
    """
    Retrieve and return device class.
    """
    device = Device(host=ip_address, user=username, password=password)
    device.open()
    return device

if __name__ == '__main__':
    ip_addr = raw_input('Enter IP address: ')
    pwd = getpass()
    user = 'pyclass'

    print 'Retrieving device facts. Please wait...  \n'
    a_device = getdevice(ip_addr, user, pwd)
    print '-' * 40
    pprint(a_device.facts)
    print
