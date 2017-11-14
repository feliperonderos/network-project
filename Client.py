from socket import *
import sys
f = open("cl.txt","w+")
f.write("hi")
f.close()
if len(sys.argv == 2):
  while True:
  	s = socket(AF_INET,SOCK_STREAM)
 	  s.connect((sys.argv[1],12001))
 	  s.send("poop".encode())
 	  reply = s.recv(1024)
 	  s.close()
