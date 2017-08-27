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

# main

# asish
print "initial balance of asish - {}".format(balance)
deposit()
print "balance after depoist - {}".format(balance)
withdraw()
print "balance after withdraw - {}".format(balance)

# sai
print "initial balance of sai - {}".format(balance)
