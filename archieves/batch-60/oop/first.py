#!/usr/bin/python

balance = 0

def my_deposit():
	global balance
	balance = balance + 1000
	return balance

def my_withdraw():
	global balance
	balance = balance - 300
	return balance

# revathi
print "initial balance for revathi {}".format(balance)
my_deposit()
print "Balance for revathi {} after deposit".format(balance)
my_withdraw()
print "Balance for revathi {} after withdraw".format(balance)

# Nanda
print "initial balance for Nanda {}".format(balance)