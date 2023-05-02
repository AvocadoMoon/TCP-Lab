##A packet can be created with various custom fields, and in scapy, they are built up in layers
##For instance, a packet with custom Ethernet, IP, and TCP fields is constructed like so:
## exPkt = Ether()/IP(dst='')/TCP(flags='')

##A few resources on scapy can be found at the following locations:
##https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf
##https://scapy.readthedocs.io/en/latest/extending.html
##https://packetlife.net/media/library/36/scapy.pdf

##You will have to specify the IP dst fields, along with the relevant TCP flags and dport fields

from scapy.all import sr1,ICMP,IP,TCP,send,DNS,UDP,DNSQR,sr
import scapy

##############Helper Communication############
##Send a packet with custom IP and TCP headers, await 1 answer, hence sr(1)
toHelper = sr1(IP(dst='HelperIP')/TCP(flags='', dport=''))

##Show the entire response packet
toHelper.show()

##Print out specific fields from specific headers in the repsponse
print(toHelper[TCP].flags)
print(toHelper[IP].id)


#####################DNS#######################
##Send a DNS request and await a DNS response
dns_req = sr1(IP(dst='HelperIP')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.google.com')), verbose=0)

##Print our a summary of the DNS related fields of the response packet
print(dns_req[DNS].summary())
