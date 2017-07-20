#!/usr/bin/python

def my_account():
	return {'balance':0}

def deposit(account):
	account['balance'] = account['balance'] + 1000
	return account['balance']

def withdraw(account):
	account['balance'] = account['balance'] - 300
	return account['balance']

# Mahesh
mahesh = my_account()
print mahesh
print "Mahesh bank balance initially is - {}  ".format(mahesh['balance'])
deposit(mahesh)
print "Mahesh bank balance after deposit is - {}  ".format(mahesh['balance'])
withdraw(mahesh)
print "Mahesh bank balance after withdraw is - {}  ".format(mahesh['balance'])

# Kaushik
kaushik = my_account()
print kaushik
print "kaushik bank balance initially is - {}  ".format(kaushik['balance'])
