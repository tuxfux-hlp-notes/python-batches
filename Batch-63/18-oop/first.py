#!/usr/bin/python

balance = 0

def deposit():
	global balance
	balance = balance + 1000
	return balance

def withdraw():
	global balance
	balance = balance - 300
	return balance

# Mahesh
print "Mahesh bank balance initially is - {}  ".format(balance)
deposit()
print "Mahesh bank balance after deposit is - {}  ".format(balance)
withdraw()
print "Mahesh bank balance after withdraw is - {}  ".format(balance)

# Kaushik
print "Kaushik bank balance initially is - {}  ".format(balance)
