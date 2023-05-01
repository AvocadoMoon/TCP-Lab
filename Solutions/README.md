# Efficient TCP Scan

The solution for this question involves the student scanning a range of ports on the victim machine utilizing crafted TCP packets using scappy.
If the response is SYN+ACK, then it is known that the port is currently open. The ports that should be open on the machine are as follows,
1049, 1308, 1700, 1800, 2000, 2020, 2590, 3164, 3250, 4000. 

### Open Telnet Ports
After the open ports are found, students should check now if these TCP ports support the Telnet application. The ports that do support it are the following
1049, 1308, 3164, and 4000.
