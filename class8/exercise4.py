#!/usr/bin/env python
"""
Exercise 4:
Remove the two objects created in the exercise3 from the database
"""

from net_system.models import NetworkDevice
import django

def main():
    """
    The main function
    """
    django.setup()

    finished_delete = False
    while finished_delete == False:
        the_device_name = raw_input("Enter device name to delete: ")
        try:
            device_to_delete = NetworkDevice.objects.get(device_name=the_device_name)
            print 'deleting %s ' % device_to_delete.device_name
            device_to_delete.delete()
        except NetworkDevice.DoesNotExist:
            print 'Device %s does not exist' % the_device_name

        delete_another = raw_input("Delete another device from the database? y or n ")
        if delete_another == 'n':
            break

if __name__ == '__main__':
    main()

