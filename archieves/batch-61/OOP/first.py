#!/usr/bin/python

balance = 0

def deposit():
	global balance
	balance = balance + 1000
	return balance

def withdraw():
	global balance
	balance = balance - 100
	return balance

# main
# Aditya

print "Balance for Aditya is {}".format(balance)
deposit()
print "Balance for Aditya is after deposit {}".format(balance)
withdraw()
print "Balance for Aditya is after withdraw {}".format(balance)

# soumitri
print "Balance for soumitri is {}".format(balance)  # 900