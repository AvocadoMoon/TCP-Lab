#!/bin/env python3
from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
import random
import telnetlib


#########################
## Find Open TCP Ports ##
#########################

def allow_tcp(pkt):
	if pkt and pkt.haslayer(IP) and pkt.haslayer(TCP):
		if pkt[TCP].flags & 0x3f == 0x12:   # SYN+ACK
			return True
		elif  pkt[TCP].flags & 4 != 0:      # RST
			raise False
		elif pkt[TCP].flags & 0x1 == 1:     # FIN
			return False
		elif pkt[TCP].flags & 0x3f == 0x10: # FIN+ACK
			return False

srcport = random.randint(1024, 65535)
ip = IP(dst="10.9.0.5")
openPorts = []

for port_number in range(2**12):
	SYN = TCP(dport=port_number, sport=srcport, flags="S", seq=1000) #Make a SYN Packet
	response = src1(ip/SYN)
	if allow_tcp(response):
		openPorts.append(port_number)


with open("open_ports.txt", "w") as op:
	op.write(openPorts)

#########################################
## Check if these ports support Telnet ##
#########################################

telnet_ports = []

for port_number in openPorts:
	try:
		telnet = telnetlib.Telnet("10.9.0.5")
		answer = telnet.read_all()
		if "User" in answer:
			telnet_ports.append(port_number)
	except:
		continue

with open("telnet_ports.txt", "w") as tp:
	tp.write(telnet_ports)
