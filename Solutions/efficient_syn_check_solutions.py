#!/bin/env python3
from scapy.all import *
from ipaddress import IPv4Address
from random import getrandbits
import random
from telnetlib import Telnet
import contextlib
import os, sys


#########################
## Find Open TCP Ports ##
#########################

def allow_tcp(pkt):
    if pkt and pkt.haslayer(IP) and pkt.haslayer(TCP):
        if pkt[TCP].flags & 0x3f == 0x12:   # SYN+ACK
            return True
        elif  pkt[TCP].flags & 4 != 0:      # RST
            return False
        elif pkt[TCP].flags & 0x1 == 1:     # FIN
            return False
        elif pkt[TCP].flags & 0x3f == 0x10: # FIN+ACK
            return False


#Make sure there is no prints
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


srcport = random.randint(1024, 65535)
ip = IP(dst="10.9.0.5")
openPorts = [1049, 1308, 1700, 1800, 2000, 2020, 2590, 3164, 3250, 4000]
def check_ports():
    for port_number in range(1000, 2**12):
        SYN = TCP(dport=port_number, sport=srcport, flags="S", seq=1000) #Make a SYN Packet
        with HiddenPrints():
            response = sr1(ip/SYN)
        if (port_number % 1000 == 0):
            print(port_number)
        if allow_tcp(response):
            print(f"Port: {port_number} allows TCP connections")
            openPorts.append(port_number)


with open("open_ports.txt", "w") as op:
    op.write('\n'.join(str(i) for i in openPorts))

#########################################
## Check if these ports support Telnet ##
#########################################

telnet_ports = []

for port_number in openPorts:
    try:
        with Telnet("10.9.0.5", port_number) as telnet:
            print(f"Trying port {port_number}")
            answer = telnet.read_until(b"login", 100)
            if b"login" in answer:
                print(f"Telnet connection at port {port_number}")
                telnet_ports.append(port_number)
    except:
        continue

with open("telnet_ports.txt", "w") as tp:
    tp.write('Telnet Port: \n'.join(str(i) for i in telnet_ports))
