#!/usr/bin/env python
"""
Use Netmiko to change the logging buffer size
on pynet-rtr2.
"""
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': password,
    'port': 8022,
}

def main():
    """
    main function
    """
#   Create router Class
    pynet2_rtr2 = ConnectHandler(**pynet2)
#   Use Netmiko to enter into router config mode
    data = pynet2_rtr2.config_mode()
#   Use Netmiko to check router prompt
    data = pynet2_rtr2.send_command("logging buffer 7777")
    pynet2_rtr2.exit_config_mode()
    data = pynet2_rtr2.send_command("show run | inc logging buffer")
    print data
    data = pynet2_rtr2.send_command("show log | inc Log Buffer")
    print data

if __name__ == "__main__":
    main()
