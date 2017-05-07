#!/usr/bin/python

def my_newaccount():
	return {'balance':0}

def my_deposit(account):
	#global balance
	account['balance'] = account['balance'] + 1000
	return account['balance']

def my_withdraw(account):
	#global balance
	account['balance'] = account['balance'] - 300
	return account['balance']

# Teja
Teja = my_newaccount()
# Teja = {'balance':0}
print Teja,type(Teja)
my_deposit(Teja)
print "amount in teja account {} after deposit".format(Teja['balance'])
my_withdraw(Teja)
print "amount in teja account {} after withdraw".format(Teja['balance'])


# venkat
venkat = my_newaccount()
print "Initial amount in venkat account {} ".format(venkat['balance'])