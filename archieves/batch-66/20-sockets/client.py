#!/usr/bin/python
# socket.AF_INET -> address family.
# socket.SOCK_STREAM -> address family type.(tcp)
# socket.SOCK_DGRAM -> address family type.(udp)
# -- client --
# socket(s) to connect to server.
# server name(www.yahoo.com).
# port name(80) -> /etc/services.
# server and port using s.connect.
# s.sendall for sending data to server.
# s.receive to receive data from the server. 


import socket
import sys

# CREATION OF SOCKET TO CONNECT TO SERVER

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,error:
	print "Failed to create a socket.Error Code: {} Error message : {}".format(str(error[0]),str(error[1]))
	sys.exit()
else:
	print 'socket created'

# connecting to a server.

host = 'www.yahoo.com'

try:
	remote_ip = socket.gethostbyname(host)
except:
	print 'Hostname could not be resolved.exiting'
	sys.exit()
else:
	print "Ip address of host is {}".format(remote_ip)

# connecting to a port
port = 80
print "connecting to the server."
s.connect((remote_ip,port))

print "socket connected to host {} on ip {}".format(host,remote_ip)

# send data to google.come
#data = raw_input("please enter some data to send to google.com:")
data= "GET / HTTP/1.1\r\n\r\n"

try:
	s.sendall(data)
except socket.error:
	print "send failed"
	sys.exit()
else:
	print "Message sending succesfully"
	reply = s.recv(4096)
	print reply