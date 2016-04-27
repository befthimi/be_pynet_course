#!/usr/bin/env python
"""
connects to router using Telnet. Returns output of "show ip int brief" command.
added some code to obtain variable command from user, but have commented this out,
as it had some caveats and wasn't what the questions asked.
added some code to strip the display of the executed command and the hostname at the
end of the output.
"""
import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def get_command_output(remote_conn, command, hostname):
    """
    Send and obtain the command output.
    Then return the output as text.
    """
    remote_conn.write(command + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    output = output.strip(command)
    output = output.strip(hostname)
    return output



def main():
    """
    the main function
    """
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    print "Attempting Telnet connection..."

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')

    time.sleep(1)
#   capture hostname to variable
    remote_conn.write('\n')
    time.sleep(1)
    hostname = remote_conn.read_very_eager()

    print "Telnet session successfully open \n"

#    command = raw_input('Enter show command here:')

#    output = get_command_output(remote_conn, command, hostname)
    output = get_command_output(remote_conn, 'show ip int brief', hostname)
    print output

    remote_conn.close()


if __name__ == "__main__":
    main()

