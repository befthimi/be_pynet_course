#!/usr/bin/env python
"""
Use Netmiko to enter into configuration mode on pynet-rtr2
Also use Netmiko to verify your state
(i.e. that you are currently in configuration mode).
"""
from getpass import getpass
from netmiko import ConnectHandler

PASSWORD = getpass()

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': PASSWORD,
    'port': 8022,
}

def inconfmode(text):
    """
    Check if in config mode.
    Return True or False.
    """
    return bool('(config)' in text)

def main():
    """
    main function
    """
#   Create router Class
    pynet2_rtr2 = ConnectHandler(**pynet2)
#   Use Netmiko to enter into router config mode
    data = pynet2_rtr2.config_mode()
#   Use Netmiko to check router prompt
    data = pynet2_rtr2.find_prompt()
    print data
    if inconfmode(data):
        print "In Configuration mode!!!"
    else:
        print "NOT in Configuration mode!!!"

if __name__ == "__main__":
    main()
