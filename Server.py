from socket import *
port = 12001
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",port))
s.listen(1)
f= open("guru99.txt","w+")
f.write("ready")
f.close()
while True:
  connectionSock, addr = s.accept()
  f= open("guru99.txt","a+")
  f.write("new connection")
  f.close()
  sentence = connectionSock.recv(1024).decode()
  f= open("guru99.txt","a+")
  f.write("new sentence" + sentence)
  f.close()
  cap = sentence.upper()
  connectionSock.send(cap.encode())
  connectionSock.close()