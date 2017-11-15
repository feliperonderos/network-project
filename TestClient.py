from socket import *
import sys
import time
import random, string

s = socket(AF_INET,SOCK_DGRAM)

time.sleep(5)
f = open("TestCounter.txt","w+")
count = 0
for i in range(100):
  try:
  	time.sleep(0.05)
  	st ="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
  	s.sendto(st.encode(),(sys.argv[1],12001))
  	s.settimeout(0.5)
  	data , addr = s.recvfrom(1024)
  	if data == st:
  		count += 1
  except:
  	pass
f.write(str(count)+ "% "+"of attempts worked\n")
f.close()