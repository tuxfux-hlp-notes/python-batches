#!/usr/bin/python

def new_account():
	return {'balance':0}

def deposit(account):
	account['balance'] = account['balance'] + 1000
	return account['balance']

def withdraw(account):
	account['balance'] = account['balance'] - 300
	return account['balance']

# main

# asish
print new_account()
asish = new_account()
print "initial balance of asish - {}".format(asish['balance'])
deposit(asish)
print "balance after depoist - {}".format(asish['balance'])
withdraw(asish)
print "balance after withdraw - {}".format(asish['balance'])

# sai
sai = new_account()
print "initial balance of sai - {}".format(sai['balance'])
