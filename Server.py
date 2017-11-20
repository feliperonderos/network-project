"""
This program initializes a single UDP Server which uses port number 12001. The server attempts to take the data it receives,
convert this to a string, capitalize the string, and send it back to the source address.
"""
from socket import *
s = socket(AF_INET,SOCK_DGRAM) #initialize UDP socket
s.bind(("",12001)) #bind socket to port 12001
while True: #loop forever while waiting for new packets
	try: #deal with errors without shutting down
	  msg, addr = s.recvfrom(1024) #receive and decode UDP packets
	  s.sendto(msg.encode().upper(),addr) #capitalize received data and send back to source.
	except:
		pass #ignore requests which crash.
