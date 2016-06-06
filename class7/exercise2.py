#!/usr/bin/env python
"""
Exercise 2:
Using Arista's pyeapi, create a script that allows you to add a VLAN
(both the VLAN ID and the VLAN name).
Then to also remove a VLAN.
Script shoul dbe idempodent.
"""
import argparse
import pyeapi

def get_pyeapi_result(data):
    '''
    Return the 'result' value from data.
    '''
    return data[0]['result']

def vlanexist(vlanid):
    """
    Check if the VLAN exists on the device.
    """
    vlantocheck = str(vlanid)
    arista_connection = pyeapi.connect_to("pynet-sw2")
    vlanapi = arista_connection.api('vlans')
    result = vlanapi.get(vlantocheck)
    if result is None:
        return False
    else:
        return True

def executecommands(commandlist):
    """
    Execute comman list parsed in.
    """
    arista_connection = pyeapi.connect_to("pynet-sw2")
    result = arista_connection.config(commandlist)
    print "Result of commmand execution: %r" % result

def addvlan(vlanname, vlanid):
    """
    function to add a VLAN
    """
    print 'Trying to add VLANID: %s with name %s' %(vlanid, vlanname)
    if vlanexist(vlanid):
        print 'VLAN exists. Nothing to do.'
    else:
        print 'VLAN does not exist. Trying to add...'
        commands = ['vlan '+str(vlanid), 'name '+vlanname]
        executecommands(commands)

def removevlan(vlanid):
    """
    function to remove a VLAN
    """
    print 'Trying to remove vlan: %s' % vlanid
    if vlanexist(vlanid):
        print 'VLAN exists. Removing...'
        commands = ['no vlan '+str(vlanid)]
        executecommands(commands)
    else:
        print 'VLAN does not exist. Nothing to do.'

def main():
    """
    Main function to add or remove a VLAN.
    """

    parser = argparse.ArgumentParser(description="Add or Remove VLAN")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--name", action="store", dest="vlanname", help="to add a VLAN")
    group.add_argument("-r", "--remove", action="store_true", help="to remove a VLAN")
    parser.add_argument("v", type=int, action="store", help="the VLAN")
    args = parser.parse_args()

    if args.vlanname:
        addvlan(args.vlanname, args.v)
    elif args.remove:
        removevlan(args.v)

if __name__ == '__main__':
    main()
