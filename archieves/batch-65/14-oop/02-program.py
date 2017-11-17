#!/usr/bin/python

def account():
	return {'balance':0}

def deposit(account):
	account['balance'] = account['balance'] + 1000
	return account['balance']

def withdraw(account):
	account['balance'] = account['balance'] - 200
	return account['balance']


# srikanth
sri = account()
print sri
# print "initial balance of sri {}".format(balance)
# deposit()
# print "After deposit balance of sri {}".format(balance)
# withdraw()
# print "After withdraw balance of sri {}".format(balance)

# # Ashok
Ashok = account()
print Ashok
# print "initial balance of ashok {}".format(balance)