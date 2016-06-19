#!/usr/bin/env python
"""
Exercise 2:
Set the vendor field of each NetworkDevice to the appropriate vendor.
Save this field to the database.
"""

from net_system.models import NetworkDevice

def main():
    """
    The main function
    """

    devices = NetworkDevice.objects.all()

    for a_device in devices:
        print a_device.device_name, a_device.vendor
        if 'pynet-sw' in a_device.device_name:
            a_device.vendor = 'Arista'
        elif 'pynet-rtr' in a_device.device_name:
            a_device.vendor = 'Cisco'
        elif 'juniper' in a_device.device_name:
            a_device.vendor = 'Juniper'
        print a_device.device_name, a_device.vendor
        a_device.save()

if __name__ == '__main__':
    main()

