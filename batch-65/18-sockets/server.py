#!/usr/bin/python
# -- server --
# opening a socket.
# bind to a address ( a server and port)
# listen to incoming connections.
# accept connections
# read/send.
# -- help --
# s.listen?
# s.bind?

#opening a socket.
import socket
from thread import start_new_thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind to a address
host='localhost'
port = 9999

try:
	s.bind((host,port))
except socket.error,msg:
	print 'Bind Failed.Error code:  - message: '.format(str(msg[0]),msg[1])
	sys.exit()
else:
	print "Binding on host {} with port {} completed".format(host,port)

# Listen to incoming connection
s.listen(10)

# send and receive data.
def clientthread(conn):
	conn.send('welcome to the server.Type something and hit enter \n')

	while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall('ok received - ' + data)
	conn.close()


while 1:
	# accept connections
	conn,addr = s.accept()
	print "connect with {} : {}".format(addr[0],str(addr[1]))
	start_new_thread(clientthread,(conn,))
	
s.close()

