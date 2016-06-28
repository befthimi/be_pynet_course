#!/usr/bin/env python
"""
    Exercise 4 class 10.
"""
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

def getdevice(ip_address, username, password):
    """
    Retrieve and return device class.
    """
    device = Device(host=ip_address, user=username, password=password)
    device.open()
    return device

if __name__ == '__main__':
    ip_addr = raw_input('Enter IP address: ')
    user = raw_input('Enter the username: ')
    pwd = getpass()

    a_device = getdevice(ip_addr, user, pwd)
    myconfig = Config(a_device)
    myconfig.lock()

    print "Test using set method"
    print "-" * 30
    myconfig.load("set system host-name pytest123", format="set", merge=True)
    print "Print difference"
    print myconfig.diff()
    print '-' * 30
    print 'Rollback'
    myconfig.rollback(0)

    print "Test using config method"
    print "-" * 30
    myconfig.load(path="test_hostname.conf", format="text", merge=True)
    print "Print difference"
    print myconfig.diff()
    print "commit changes"
    myconfig.commit(comment="Testing conf commit BE")

    print "Test using xml method"
    print "-" * 30
    myconfig.load(path="test_hostname.xml", format="xml", merge=True)
    print "Print difference"
    print myconfig.diff()
    print "commit changes"
    myconfig.commit(comment="Testing xml commit BE")

    myconfig.unlock()
