#!/usr/bin/env python
"""
retrieve "change logging buffer to 10240 using pexpect"
"""
from getpass import getpass
import pexpect

def logmein(username, ip_addr, port, password):
    """
    login to remote device
    """
    connection = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    connection.timeout = 3
    connection.expect('assword:')
    connection.sendline(password)
    connection.expect('#')
    return connection

def main():
    """
    main function
    """
    ip_addr = '50.76.53.27'
    username = raw_input('Please Enter Username: ')
    password = getpass()
    port = 8022

    ssh_conn = logmein(username, ip_addr, port, password)
    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')
    ssh_conn.sendline('logging buffer 10240')
    ssh_conn.sendline('end')
    ssh_conn.expect('pynet-rtr2#')
    ssh_conn.sendline('show log | inc Log Buffer')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before
    ssh_conn.sendline('show run | inc logging buffer')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before

if __name__ == "__main__":
    main()
