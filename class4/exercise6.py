#!/usr/bin/env python
"""
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
"""
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()
pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'port': 8022,
}

juniper_srx = {
    'device_type': 'juniper',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'port': 9822,
}

def main():
    """
    main function
    """
    pynet_R1 = ConnectHandler(**pynet1)
    pynet_R2 = ConnectHandler(**pynet2)
    srx = ConnectHandler(**juniper_srx)
    arp_r1 = pynet_R1.send_command("show arp")
    arp_r2 = pynet_R2.send_command("show arp")
    arp_srx = srx.send_command("show arp")
    print '-' * 8
    print 'SHOW ARP:'
    print '-' * 8
    print '\npynet-rtr1:'
    print arp_r1
    print '\npynet-rtr2:'
    print arp_r2
    print '\njuniper_srx:'
    print arp_srx
    print '=' * 8

if __name__ == "__main__":
    main()
