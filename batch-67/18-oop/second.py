#!/usr/bin/python

def my_account():
	return {'balance':0}

def  my_deposit(account):
	account['balance'] = account['balance'] + 1000
	return account['balance']

def my_withdraw(account):
	account['balance'] = account['balance'] - 300
	return account['balance']

# main
## balu
balu = my_account()
print balu
print "Balus initial balance is {}".format(balu['balance'])
my_deposit(balu)
print "Balus balance {} after deposit".format(balu['balance'])
my_withdraw(balu)
print "Balus balance {} after withdraw".format(balu['balance'])

## ravi
ravi = my_account()
print "ravi's initial balance {}".format(ravi['balance'])
