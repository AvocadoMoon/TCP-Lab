## Use this file to generate random TCP ports to open on victim docker container
## This file configures the container to open 4 more telnet ports, and 5 other raw TCP ports
## Port numbers are written in inetd2.conf and services2 to preserve original files
## These two files are used when starting the victim container to open the randomized ports

import random

## Create random port numbers for raw TCP ports in inetd.conf
with open("./inetd.conf", "r") as f:
    data = f.read()

    for i in range(5, 11):
        overwritestr = "##portnumber" + str(i)
        data = data.replace(overwritestr, str(random.randint(2000, 65000)))

    with open("./inetd2.conf", "w") as new:
        new.write(data)
        
## Create randon port numbers for telnet TCP services        
with open("./services", "r") as f:
    data = f.read()
    
    for i in range(1, 5):
    	overwritestr = "##portnumber" + str(i)
    	data = data.replace(overwritestr, str(random.randint(2000, 65000)) + "/tcp")
    	
    with open("./services2", "w") as new:
    	new.write(data)
