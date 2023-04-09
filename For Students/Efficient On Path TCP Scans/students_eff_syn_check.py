#!/bin/env python3
from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
import random
import telnetlib


#########################
## Find Open TCP Ports ##
#########################


#---Helper that checks TCP responses---#
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

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout



srcport = random.randint(@@@@, @@@@)
ip = IP(dst="@@@@")
openPorts = []

for port_number in range(@@@@):
    SYN = TCP(dport=port_number, sport=scrport, flags="S", seq=1000)
    with HiddenPrints():
        response = src1(ip/SYN) #Sends packet, then gets a response


#########################################
## Check if these ports support Telnet ##
#########################################

telnet_ports = []

for port_number in openPorts:
    try:
        with telnetlib.Telnet("@@@@") as telnet:
            telnet.read_until("@@@", @@@)
    except:
        continue









