from socket import *
import sys
if (len(sys.argv) == 3):
  while True:
  	s = socket(AF_INET,SOCK_STREAM)
  	s.connect((sys.argv[1],12001))
  	s.send("poop".encode())
  	reply = s.recv(1024)
  	f = open("cl.txt","a+")
  	f.write(reply + sys.argv[2])
  	f.close()
  	s.close()
