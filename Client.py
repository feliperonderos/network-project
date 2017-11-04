from socket import *
import sys
if len(sys.argv == 2):
  while True:
  	s = socket(AF_INET,SOCK_STREAM)
 	  s.connect((sys.argv[1],12001))