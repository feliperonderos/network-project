from socket import *
messages = {}
port = 12001
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",port))
s.listen(5)
while True:
  connectionSock, addr = s.accept()
  msg = ""
  while msg != "END":
  	msg = connectionSock.recv(1024).decode()
  	if addr in messages:
  		messages[addr].append(msg)
  	else:
  		messages[addr] = [msg]
  connectionSock.close()