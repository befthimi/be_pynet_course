#!/usr/bin/env python
"""
Exercise 1:
Use Arista's eAPI to obtain 'show interfaces' from the switch.
Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields
for each of the interfaces on the switch.
Accomplish this using Arista's pyeapi.
"""
import pyeapi

def get_pyeapi_result(data):
    '''
    Return the 'result' value from data.
    '''
    return data[0]['result']

def main():
    """
    main function of get octet stats from Arista switch interfaces
    """
    arista_connection = pyeapi.connect_to("pynet-sw2")
    interfaces = arista_connection.enable("show interfaces")
    interfaces = get_pyeapi_result(interfaces)
    interfaces = interfaces['interfaces']

    print '{:20s} {:>20s} {:>20s}'.format('Interface Label', 'InOctets', 'OutOctets')

    for interface in interfaces:
        intf = interfaces[interface]
        if intf.__contains__('interfaceCounters'):
            intfcnters = intf['interfaceCounters']
            inbytes = intfcnters['inOctets']
            outbytes = intfcnters['outOctets']
            print '{:20s} {:20d} {:20d}'.format(interface, inbytes, outbytes)
        else:
            print '{:20s} {:>20s} {:>20s}'.format(interface, 'None', 'None')

if __name__ == '__main__':
    main()
