#!/usr/bin/python3
import socket
import argparse
import sys

def portscan(host):
    for port in range(1,65535):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Establishing connection to ports
                s.connect((host, port))
                print("Open port: {}".format(port))
                # Close the connection after connecting the socket
                s.close()
                # Save the output of open ports to a file
                open_ports = open('open_ports.txt', 'a')
                open_ports.write(str(port) + '\n')
                open_ports.close()
        except KeyboardInterrupt:
            print("Process Interrupted by The User")
            sys.exit()
        except socket.error:
            s.close()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--IP", required=True)
args = parser.parse_args()
portscan(sys.argv[2])