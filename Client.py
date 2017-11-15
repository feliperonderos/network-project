from socket import *
import random, string
import sys
if (len(sys.argv) == 3):
  while True:
  	p ="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000))
  	print p
  	s = socket(AF_INET,SOCK_STREAM)
  	s.connect((sys.argv[1],12001))
  	while True:
  		s.send(p.encode())
  	s.close()
