from socket import *
port = 12001
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",port))
f= open("guru99.txt","w+")
f.write("poop")
f.close()
s.listen(1)
while True:
  connectionSock, addr = s.accept()
  print "New connection"
  sentence = connectionSock.recv(1024).decode()
  cap = sentence.upper()
  connectionSock.send(cap.encode())
  connectionSock.close()