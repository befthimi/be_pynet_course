#!/usr/bin/env python
"""
Use Netmiko to change the logging buffer size
and to disable console logging
from a file on both pynet-rtr1 and pynet-rtr2
"""
import os
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

def changelogbehaviour(rclass):
    """
    Change the logging behaviour
    """
    rclass.send_config_from_file(config_file='config_file.txt')
    data = rclass.find_prompt()
    print '\n'
    print data
    print "-" * 8
    data = rclass.send_command("show run | inc logging buffer")
    print data
    data = rclass.send_command("show run | inc logging console")
    print data

def main():
    """
    main function
    """
# Clear screen of rubbish and print friendly message
    os.system('clear')
    print "Please Wait..."

    pynet_R1 = ConnectHandler(**pynet1)
    pynet_R2 = ConnectHandler(**pynet2)
    changelogbehaviour(pynet_R1)
    changelogbehaviour(pynet_R2)

if __name__ == "__main__":
    main()
