#!/usr/bin/env python
"""
    Exercise 2 class 10.
"""
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass

def getdevice(ip_address, username, password):
    """
    Retrieve and return device class.
    """
    device = Device(host=ip_address, user=username, password=password)
    device.open()
    return device

def getports(thedevice):
    """
    Retrieve ports list
    """
    ports = EthPortTable(thedevice)
    ports.get()
    return ports

if __name__ == '__main__':
    ip_addr = raw_input('Enter IP address: ')
    pwd = getpass()
    user = 'pyclass'
    print 'Retrieving device interface. Please wait...  \n'
    a_device = getdevice(ip_addr, user, pwd)
    print '-' * 98
    myports = getports(a_device)

    print '%18s %22s %26s %26s' % ('Interface Name', 'Oper State', 'In Packets', 'Out Packets')
    print '-' * 98
    for item in myports.items():
        print "%18s, %22s, %26s, %26s" % (item[0], item[1][0], item[1][1], item[1][10])

    print
