#!/usr/bin/python

# blueprint
# class Account(object):
# class Account:
class Account:
	balance = 0

# sri
print Account
print type(Account) # <type 'classobj'>
print type(Account())

# variables/data
# class variables and instance variables

sri = Account
print type(sri),dir(sri)
sri.balance = 1000
print sri.balance

Ashok = Account()
print type(Ashok),dir(Ashok)
print Ashok.balance
Ashok.balance = 2000
print Ashok.balance



# bibha

ansh = Account()
ansh.balance = 100
print ansh.balance

bibha = Account
print type(bibha),dir(bibha)
print bibha.balance
