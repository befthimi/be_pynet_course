#!/usr/bin/env python
"""
Script that detects router configuration changes.
"""
import pickle
import os
import datetime
import email_helper
import snmp_helper

SYSUPTIMEOID = '1.3.6.1.2.1.1.3.0'
SYSDESCR = '1.3.6.1.2.1.1.1.0'
SYSNAME = '1.3.6.1.2.1.1.5.0'
RUNNINGLASTCHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
RUNNINGLASTSAVED = '1.3.6.1.4.1.9.9.43.1.1.2.0'
STARTUPLASTCHANGED = '1.3.6.1.4.1.9.9.43.1.1.3.0'
ROUTER1 = ('50.76.53.27', 7961)
ROUTER2 = ('50.76.53.27', 8061)
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)

def send_email(datetimestr, hostname):
    """
    Sends an Email to my gmail account
    """
    recipient = 'bill.efthimiou@gmail.com'
    subject = 'Router Config change alert'
    message = '''

    Router Running Configuration change - ALERT

    Change: %r
    Router Name: %s

    ''' % (datetimestr, hostname)

    sender = 'bill_efthimiou@hotmail.com'
    email_helper.send_mail(recipient, subject, message, sender)

def snmp_get(whichrouter, which_oid):
    """
    Get snmp result based on which router and OID
    """
    snmp_data = snmp_helper.snmp_get_oid_v3(whichrouter, snmp_user, oid=which_oid)
    snmp_result = snmp_helper.snmp_extract(snmp_data)
    return snmp_result

if os.path.isfile("router1.pkl"):
    router_file = open("router1.pkl", "r+b")
    if os.stat("router1.pkl").st_size != 0:
        file_data = pickle.load(router_file)
        print file_data
        current_timestamp = (snmp_get(ROUTER2, RUNNINGLASTCHANGED))
        if current_timestamp > file_data:
            router_file.close()
            #close the file and reopen as write clearing previous contents.
            router_file = open("router1.pkl", "wb")
            print "Router configuration has changed"
            file_data = current_timestamp
            pickle.dump(file_data, router_file, -1)
            timestamp = datetime.datetime.fromtimestamp(int(file_data))
            print timestamp.strftime("%A, %d. %B %Y, %H:%M:%S")
            devicename = (snmp_get(ROUTER2, SYSNAME))
            send_email(timestamp.strftime("%A, %d. %B %Y, %H:%M:%S"), devicename)
        else:
            print "No change to router config."

    else:
        file_data = (snmp_get(ROUTER2, RUNNINGLASTCHANGED))
        pickle.dump(file_data, router_file, -1)
else:
    router_file = open("router1.pkl", "wb")
    print "create new file"
    file_data = (snmp_get(ROUTER2, RUNNINGLASTCHANGED))
    pickle.dump(file_data, router_file, -1)

router_file.close()
