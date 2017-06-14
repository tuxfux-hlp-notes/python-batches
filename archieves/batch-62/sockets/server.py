#!/usr/bin/python
'''
a) Opening a socket.
b) Bind to address and port.
c) Listen to incoming connections.
d) Accept connections.
e) Read/send data.


'''

import sys,socket

HOST = 'localhost'
PORT = 9002
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
  s.bind((HOST, PORT))
except socket.error, msg:
  print 'Bind Failed. Error code : ' + str(msg[0]) + ' message ' + msg[1]
  sys.exit()

print 'Socket binding completed'

s.listen(10)
print 'socket now listening on port {}'.format(PORT)

conn,addr = s.accept()

print "connected with" +  addr[0] + ':' + str(addr[1])


data = conn.recv(1024) # receiving the data from the client.
conn.sendall('ok , i am doing great.. How about a cup of coffee ?')     #  send the data batk to the client.


conn.close()
s.close()


