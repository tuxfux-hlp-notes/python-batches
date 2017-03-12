#!/usr/bin/python

def account():
	return {'balance':0}

def deposit(account,amount):
	account['balance'] = account['balance'] + amount
	return account['balance']

def withdraw(account,amount):
	account['balance'] = account['balance'] - amount
	return account['balance']

# Ranjith
Ranjith = account()
print "Initial balance of Ranjith {}".format(Ranjith['balance'])
print "depositing some 1000 rs."
deposit(Ranjith,1000)
print "Balance of Ranjith {} after deposit".format(Ranjith['balance'])
withdraw(Ranjith,500)
print "Balance of Ranjith {} after withdraw".format(Ranjith['balance'])

# Raj
Raj = account()
print "Initial balance of Raj {}".format(Raj['balance'])
