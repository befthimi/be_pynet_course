#!/usr/bin/env python
"""
Exercise 1b:
Update the NetworkDevice objects such that each NetworkDevice links to the correct Credentials.
"""

from net_system.models import NetworkDevice, Credentials

def main():
    """
    The main function
    """

    devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    standard_creds = creds[0]
    arista_creds = creds[1]

    for a_device in devices:
        if 'pynet-sw' in a_device.device_name:
            a_device.credentials = arista_creds
            print a_device.device_name, a_device.credentials
        else:
            a_device.credentials = standard_creds
            print a_device.device_name, a_device.credentials
        a_device.save()

if __name__ == '__main__':
    main()

