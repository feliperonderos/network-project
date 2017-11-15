from socket import *
import sys
import time
import random, string

s = socket(AF_INET,SOCK_DGRAM)
succ = 0
att = 0
while True:
  try:
  	att += 1
  	st ="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
  	s.sendto(st.encode(),(sys.argv[1],12001))
  	s.settimeout(0.5)
  	data , addr = s.recvfrom(1024)
  	if data == st:
  		succ += 1
  		f = open("TestCounter.txt","w+")
  		f.write(str(succ) +" of "+ str(att) +" attempts worked\n")
  		f.close()
  except:
  	pass
