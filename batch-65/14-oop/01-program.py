#!/usr/bin/python

balance=0

def deposit():
	global balance
	balance = balance + 1000
	return balance

def withdraw():
	global balance
	balance = balance - 200
	return balance

# srikanth
print "initial balance of sri {}".format(balance)
deposit()
print "After deposit balance of sri {}".format(balance)
withdraw()
print "After withdraw balance of sri {}".format(balance)

# Ashok
print "initial balance of ashok {}".format(balance)
