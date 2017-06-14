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

# rakesh
print "inital balance of rakesh {}".format(balance)
deposit(1000)
print "balance after deposit of 1000 is {}".format(balance)
withdraw(300)
print "balance after withdraw of 300 is {}".format(balance)

# akshay
print "inital balance of akhay {}".format(balance)