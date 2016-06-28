#!/usr/bin/env python
"""
    Exercise 3 class 10.
"""
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass
from pprint import pprint

def getdevice(ip_address, username, password):
    """
    Retrieve and return device class.
    """
    device = Device(host=ip_address, user=username, password=password)
    device.open()
    return device

def getroutes(thedevice):
    """
    Retrieve routing table
    """
    routes = RouteTable(thedevice)
    routes.get()
    return routes

if __name__ == '__main__':
    ip_addr = raw_input('Enter IP address: ')
    pwd = getpass()
    user = 'pyclass'

    a_device = getdevice(ip_addr, user, pwd)
    myroutes = getroutes(a_device)
    print '-' * 40
    for item in myroutes.items():
        pprint(item)
        print

    print
