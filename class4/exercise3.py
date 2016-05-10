#!/usr/bin/env python
"""
retrieve "show Ip int brief using pexpect"
"""
from getpass import getpass
import pexpect

def main():
    """
    main function
    """
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = getpass()
    port = 8022

    print 'Spawning SSH connection..........'
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    print 'Waiting for expect....'
#    ssh_conn.expect('you sure you want to continue connecting (yes/no)?')
#    print 'Got expect'
#    print ssh_conn.before
#    print ssh_conn.after
#    ssh_conn.sendline('yes')
    ssh_conn.expect('assword:')
    print 'got password prompt'
    print 'Sending password %s' % password
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('pynet-rtr2#')
    print ssh_conn.before

if __name__ == "__main__":
    main()
