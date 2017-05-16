#!/usr/bin/python

def my_account():
	return {'balance':0}

def deposit(account):
	account['balance'] = account['balance']  + 1000
	return account['balance'] 

def withdraw(account):
	account['balance']  = account['balance']  - 100
	return account['balance'] 

# Aditya
aditya = my_account()
print aditya
deposit(aditya)
print "balance of aditya after deposit {}".format(aditya['balance'])
withdraw(aditya)
print "balance of aditya after withdraw {}".format(aditya['balance'])

# soumitri
soumitri = my_account()
print soumitri