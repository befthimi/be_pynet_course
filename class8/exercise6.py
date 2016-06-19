#!/usr/bin/env python
"""
Exercise 6:
Use threads and Netmiko to execute 'show version' on each device in the database.
Calculate the amount of time required to do this.
What is the difference in time between executing 'show version' sequentially
versus using threads?
"""
import time
import threading
from netmiko import ConnectHandler
from net_system.models import NetworkDevice
import django

def show_version(device):
    """
    Function to get output of 'show version'.
    """

    remote_connection = ConnectHandler(device_type=device.device_type,
                                        ip=device.ip_address, port=device.port,
                                        username=device.credentials.username,
                                        password=device.credentials.password)
    print '=' * 50
    print device.device_name
    print '-' * 15
    print remote_connection.send_command_expect('show version')

def main():
    """
    The main function
    """
    django.setup()

    device_list = NetworkDevice.objects.all()
    starttime = time.time()

    for device in device_list:
        device_thread = threading.Thread(target=show_version, args=(device,))
        device_thread.start()

    main_thread = threading.currentThread()
    for a_thread in threading.enumerate():
        if a_thread != main_thread:
            print a_thread
            a_thread.join()

    finishtime = time.time()
    total_elapsed_time = finishtime - starttime  

    print '*' * 50
    print 'Overall retrieval time: %.2f seconds' % round(total_elapsed_time, 2)
    print '*' * 50

if __name__ == '__main__':
    main()

