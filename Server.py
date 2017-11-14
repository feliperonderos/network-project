from socket import *
port = 12001
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",port))
s.listen(1)
f= open("guru99.txt","w+")
f.write("pppppaap")
f.close()
while True:
  connectionSock, addr = s.accept()
  f= open("guru99.txt","w+")
  
  f.close()
  sentence = connectionSock.recv(1024).decode()
  cap = sentence.upper()
  connectionSock.send(cap.encode())
  connectionSock.close()