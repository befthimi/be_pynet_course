#!/usr/bin/env python
"""
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.
"""
import time
from getpass import getpass
import paramiko
IP_ADDRESS = '50.76.53.27'
USERNAME = 'pyclass'
PASSWORD = getpass()
PORT = 8022

def get_showver(connection):
    """
    Get the show version output and display on screen
    with no terminal paging
    """
    connection.settimeout(5.0)
    connection.send("terminal length 0\n")
    data_buffer = connection.send("show version\n")
    time.sleep(2)
    data_buffer = connection.recv(5000)
    print data_buffer

def main():
    """
    The main function
    """
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(IP_ADDRESS, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False, port=PORT)
    remote_conn = remote_conn_pre.invoke_shell()

    get_showver(remote_conn)

if __name__ == "__main__":
    main()
