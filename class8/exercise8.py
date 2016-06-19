#!/usr/bin/env python
"""
Exercise 8. use a queue to get the output data back from the child processes in question #7.
Print this output data to the screen in the main process.
"""
import time
from multiprocessing import Process, current_process, Queue
from netmiko import ConnectHandler
from net_system.models import NetworkDevice
import django

def show_version_queue(device, q):
    """
    Function to get output of 'show version'.
    """
    output_dict = {}
    remote_connection = ConnectHandler(device_type=device.device_type,
                                       ip=device.ip_address, port=device.port,
                                       username=device.credentials.username,
                                       password=device.credentials.password)
    output = ('=' * 80)
    output += ('\n')
    output += remote_connection.send_command_expect('show version')
    output_dict[device.device_name] = output
    q.put(output_dict)

def main():
    """
    The main function
    """
    django.setup()

    device_list = NetworkDevice.objects.all()
    q = Queue(maxsize=20)
    starttime = time.time()

    procs_list = []
    for device in device_list:
        device_proc = Process(target=show_version_queue, args=(device, q))
        device_proc.start()
        procs_list.append(device_proc)

    for a_proc in procs_list:
        print a_proc
        a_proc.join()

    while not q.empty():
        my_dict = q.get()
        for k, v in my_dict.iteritems():
            print k
            print v

    finishtime = time.time()
    total_elapsed_time = finishtime - starttime

    print '*' * 50
    print 'Overall retrieval time: %.2f seconds' % round(total_elapsed_time, 2)
    print '*' * 50

if __name__ == '__main__':
    main()

