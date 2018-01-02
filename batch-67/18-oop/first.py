#!/usr/bin/python

balance  = 0

def  my_deposit():
	global balance
	balance = balance + 1000
	return balance

def my_withdraw():
	global balance
	balance = balance - 300
	return balance

# main
## balu
print "Balus initial balance is {}".format(balance)
my_deposit()
print "Balus balance {} after deposit".format(balance)
my_withdraw()
print "Balus balance {} after withdraw".format(balance)

## ravi
print "ravi's initial balance {}".format(balance)
