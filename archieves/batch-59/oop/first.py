#!/usr/bin/python

balance = 0

def deposit(amount):
	global balance
	balance = balance + amount
	return balance

def withdraw(amount):
	global balance
	balance = balance - amount
	return balance

# Ranjith
print "my initial balance {}".format(balance)
print " i am depositing 1000 rs to Ranjith"
deposit(1000)
print "my  balance after deposti{}".format(balance)
print " i am with drawing 500 rs of Ranjith"
withdraw(500)
print "my balance {} after withdraw".format(balance)

# Raj
print "my initial balance {}".format(balance)