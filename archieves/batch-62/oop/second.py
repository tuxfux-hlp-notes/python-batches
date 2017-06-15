#!/usr/bin/python

def account():
	return {'balance':0}

def deposit(account,amount):
	account['balance'] = account['balance'] + amount
	return account['balance']

def withdraw(account,amount):
	account['balance'] = account['balance'] - amount
	return account['balance']

# varun
varun = account()
print "initial balance of varun is {}".format(varun['balance'])
deposit(varun,1000)
print "balance of varun is {}".format(varun['balance'])
withdraw(varun,100)
print "balance of varun is {}".format(varun['balance'])

# vishnu
vishnu = account()
print "initial balance of vishnu is {}".format(vishnu['balance'])