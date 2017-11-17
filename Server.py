from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",12001))
while True:
	try:
	  msg, addr = s.recvfrom(1024)
	  s.sendto(msg.encode().upper(),addr)
	except:
		pass





	"""
from socket import *
messages = {}
port = 12001
s = socket(AF_INET,SOCK_STREAM)
s.bind(("localhost",port))
s.listen(5)
while True:
  connectionSock, addr = s.accept()
  msg = ""
  while msg != "END":
  	msg = connectionSock.recv(1024).decode()
  	print msg
  	if addr in messages:
  		messages[addr].append(msg)
  	else:
  		messages[addr] = [msg]
  connectionSock.close()




import socket
from threading import Thread
from SocketServer import ThreadingMixIn
 
class ClientThread(Thread):
  def __init__(self,ip,port):
	  Thread.__init__(self)
	  self.ip = ip
	  self.port = port
  def run(self):
    while True:
    	data = conn.recv(2048)
    	if not data: break
    	print "received data:", data
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 12001))
threads = []
 
while True:
    s.listen(4)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = s.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)
 
for t in threads:
    t.join()
"""