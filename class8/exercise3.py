#!/usr/bin/env python
"""
Exercise 3:
Create two new test NetworkDevices in the database.
Use both direct object creation and the .get_or_create() method to create the devices.
"""

from net_system.models import NetworkDevice
import django

def main():
    """
    The main function
    """
    django.setup()

    pynet_rtr3 = NetworkDevice(
        device_name='pynet-rtr3',
        device_type='cisco_ios',
        ip_address='192.168.100.1',
        port=22,
    )
    pynet_rtr3.save()

    pynet_rtr4 = NetworkDevice.objects.get_or_create(
        device_name='pynet-rtr4',
        device_type='cisco_ios',
        ip_address='10.10.10.10',
        port=22,
    )
    print pynet_rtr4


if __name__ == '__main__':
    main()

