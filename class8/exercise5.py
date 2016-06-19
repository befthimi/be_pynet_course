#!/usr/bin/env python
"""
Exercise 5:
Use Netmiko to connect to each of the devices in the database.
Execute 'show version' on each device.
"""
import time
from netmiko import ConnectHandler
from net_system.models import NetworkDevice
import django

def main():
    """
    The main function
    """
    django.setup()

    total_elapsed_time = 0
    device_list = NetworkDevice.objects.all()

    for device in device_list:
        starttime = time.time()
        remote_connection = ConnectHandler(device_type=device.device_type,
                                           ip=device.ip_address, port=device.port,
                                           username=device.credentials.username,
                                           password=device.credentials.password)
        print '=' * 50
        print device.device_name
        print '-' * 15
        print remote_connection.send_command_expect('show version')
        finishtime = time.time()
        timedelta = finishtime - starttime
        total_elapsed_time = total_elapsed_time + timedelta
        print 'Retrieval duration: %.2f seconds' % round(timedelta, 2)
        print

    print '*' * 50
    print 'Overall retrieval duration: %.2f seconds' % round(total_elapsed_time, 2)
    print '*' * 50

if __name__ == '__main__':
    main()

