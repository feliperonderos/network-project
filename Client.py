from socket import *
import sys
f = open("cl.txt","a+")
f.write(str(sys.argv[1]))
f.close()
if len(sys.argv == 2):
  while True:
  	s = socket(AF_INET,SOCK_STREAM)
 	  s.connect((sys.argv[1],12001))
 	  s.send("poop".encode())
 	  reply = s.recv(1024)
 	  f = open("cl.txt","a+")
 	  f.write(reply)
 	  f.close()
 	  s.close()
