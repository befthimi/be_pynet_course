#!/usr/bin/env python
"""
Exercise 7. Repeat exercise #6 except use processes.
"""
import time
from multiprocessing import Process, current_process
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

    procs_list = []
    for device in device_list:
        device_proc = Process(target=show_version, args=(device,))
        device_proc.start()
        procs_list.append(device_proc)

    for a_proc in procs_list:
        print a_proc
        a_proc.join()

    finishtime = time.time()
    total_elapsed_time = finishtime - starttime  

    print '*' * 50
    print 'Overall retrieval time: %.2f seconds' % round(total_elapsed_time, 2)
    print '*' * 50

if __name__ == '__main__':
    main()

