from socket import *
port = 12001
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",port))
s.listen(5)
while True:
  connectionSock, addr = s.accept()
  sentence = ""
  while (sentence != "END"):
  	sentence = connectionSock.recv(1024).decode()
  	cap = sentence.upper()
  	connectionSock.send(cap.encode())
  connectionSock.close()