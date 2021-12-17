#Aneliz Vargas
#Port Scanner Project
#!/usr/bin/env Python 3.10)

#some sources that helped me:
#https://www.geeksforgeeks.org/python-simple-port-scanner-with-sockets/
#https://stackoverflow.com/questions/9252373/random-iteration-in-python
#https://www.geeksforgeeks.org/python-sys-module/
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
#https://stackoverflow.com/questions/58569361/attributeerror-module-time-has-no-attribute-clock-in-python-3-8
#https://johanneskinzig.de/index.php/it-security/12-port-scanning-and-banner-grabbing-with-python


import socket
import sys
import random
import time

ip = socket.gethostbyname (sys.argv[2])
openPorts = []
closedPorts = []
isAlive = 0

def bannerGrabber(addr, port):
    print('banner for port: ', port)
    bannerGrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        bannerGrab.connect((addr, port))
        bannerGrab.send('WhoAreYou\r\n')
        banner = bannerGrab.recv(100)
        bannerGrab.close()
        print(banner, "\n")
    except:
        print('Cannot connect to port ', port)

#this will basically check if the ip address is alive because if it isn't,
#then it would print out unknown host
try:
    socket.gethostbyaddr(ip)
    isAlive = 1
except socket.herror:
    print ('Unknown host')


def sequentialOrder():
    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # create a new socket
            serv.bind((ip,port)) # bind socket with address
            service = socket.getservbyport()
            openPorts.append(port)
            print(port, '\t open \t', service)
            bannerGrabber(ip, port)
            
        except:
            closedPorts.append(port) 
        
        serv.close() #close connection
    
def randomOrder():
    r = list(range(65535))
    random.shuffle(r)
    
    for port in r:
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # create a new socket
            serv.bind((ip,port)) # bind socket with address
            service = socket.getservbyport()
            openPorts.append(port)
            print(port, '\t open \t', service)
            bannerGrabber(ip, port)
        except:
            closedPorts.append(port) 
        serv.close() #close connection

def allPorts():
    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # create a new socket
            serv.bind((ip,port)) # bind socket with address
            service = socket.getservbyport()
            openPorts.append(port)
            print(port, '\t open \t', service)
            bannerGrabber(ip, port)
        except:
            closedPorts.append(port) 
        serv.close() #close connection

def knownPorts():
    wellKnown = [80, 443, 20, 21, 22, 5060, 53, 25, 110, 143, 23, 119, 563, 194, 123, 514, 88, 137, 138, 139]
    for port in wellKnown:
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # create a new socket
            serv.bind((ip,port)) # bind socket with address
            service = socket.getservbyport()
            openPorts.append(port)
            print(port, '\t open \t', service)
            bannerGrabber(ip, port)
        except:
            closedPorts.append(port) 
        serv.close() #close connection

if isAlive == 1:
    if sys.argv[1] == "order":
        start_time = time.process_time()
        print('PORT \t STATE \t SERVICE')
        sequentialOrder();
        timeTook = time.process_time()- start_time
        print('scan done! 1 IP address (1 host up) scanned in ', timeTook)
        print('Shown: ', len(openPorts), ' open ports')
        print('Not Shown: ', len(closedPorts), ' closed ports')
        
        
    elif sys.argv[1] == "random":
        start_time = time.process_time()
        print('PORT \t STATE \t SERVICE')
        randomOrder();
        timeTook = time.process_time()- start_time
        print('scan done! 1 IP address (1 host up) scanned in ', timeTook)
        print('Shown: ', len(openPorts), ' open ports')
        print('Not Shown: ', len(closedPorts), ' closed ports')
        
    elif sys.argv[1] == "all":
        start_time = time.process_time()
        print('PORT \t STATE \t SERVICE')
        allPorts();
        timeTook = time.process_time()- start_time
        print('scan done! 1 IP address (1 host up) scanned in ', timeTook)
        print('Shown: ', len(openPorts), ' open ports')
        print('Not Shown: ', len(closedPorts), ' closed ports')
        
    elif sys.argv[1] == "known":
        start_time = time.process_time()
        print('PORT \t STATE \t SERVICE')
        knownPorts();
        timeTook = time.process_time()- start_time
        print('scan done! 1 IP address (1 host up) scanned in ', timeTook)
        print('Shown: ', len(openPorts), ' open ports')
        print('Not Shown: ', len(closedPorts), ' closed ports')



