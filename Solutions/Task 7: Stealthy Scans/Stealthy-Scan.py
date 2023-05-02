##A packet can be created with various custom fields, and in scapy, they are built up in layers
##For instance, a packet with custom Ethernet, IP, and TCP fields is constructed like so:
## exPkt = Ether()/IP(dst='')/TCP(flags='')

##A few resources on scapy can be found at the following locations:
##https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf
##https://scapy.readthedocs.io/en/latest/extending.html
##https://packetlife.net/media/library/36/scapy.pdf

from scapy.all import sr1,ICMP,IP,TCP,send,DNS,UDP,DNSQR,sr

##Will have to specify the IP dst fields, along with the relevant TCP flags and dport fields

###############Packet Spoofing#################
##Spoof packet with custom source addr

##Send but do not await a response for our spoofed packet
toHost = send(IP(src='HelperIP', dst='ScannedIP')/TCP(flags='', dport=''))
toHost.show()

##########Communicating with the Helper########

###Two methods
##Method 1: DNS requests
dns_req = sr1(IP(dst='HelperIP')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.google.com')), verbose=0)
dns_req.show()
print("ID for DNS response is: " + str(dns_req[IP].id))

##Method 2: Half-open TCP connection
toHelper = sr1(IP(dst='HelperIP')/TCP(flags='', dport=''))
closeConnection = send(IP(dst='HelperIP')/TCP(flags='F', dport=''))
toHelper.show()

