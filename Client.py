from socket import *
import sys
if (len(sys.argv) == 3):
  while True:
  	s = socket(AF_INET,SOCK_STREAM)
  	s.connect((sys.argv[1],12001))
  	p =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000))
  	while True:
  	  s.send(p.encode())
  		s.recv(1024)
   	s.close()
