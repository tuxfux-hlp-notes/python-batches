#!/usr/bin/python

balance=0

def my_withdraw():
	global balance
	balance = balance - 200
	return balance

def my_deposit():
	global balance
	balance = balance + 1000
	return balance

# Main
print "initial balance - {}".format(balance)
my_deposit()
print "after deposit balance - {}".format(balance)
my_withdraw()
print "after withdraw balance - {}".format(balance)