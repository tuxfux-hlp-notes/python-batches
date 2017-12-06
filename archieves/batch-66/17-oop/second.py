#!/usr/bin/python

def my_account():
	return {'balance':0}

def deposit(account):
    account['balance'] = account['balance'] + 1000
    return account['balance']

def withdraw(account):
	account['balance'] = account['balance'] - 200
	return account['balance']

def my_balance(account):
	return account['balance']

# saleem
saleem = my_account()
print "balance of saleem before deposit {}".format(my_balance(saleem))
deposit(saleem)
print "balance of saleem after deposit {}".format(my_balance(saleem))
withdraw(saleem)
print "balance of saleem after withdraw {}".format(my_balance(saleem))

# navya
navya = my_account()
print "balance of navya before deposit {}".format(my_balance(navya))