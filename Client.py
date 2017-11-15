from socket import *
import time
import random, string
import sys
if (len(sys.argv) == 3):
  while True:
    try:
	    p ="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000))
	    #p = sys.argv[2]
	    s = socket(AF_INET,SOCK_STREAM)
	    s.connect((sys.argv[1],12001))
	    while True:
	    	s.send(p.encode())
    except:
	  	s.close()