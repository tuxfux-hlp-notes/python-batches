#!/usr/bin/python

'''
# example 2:
# function are methods in your class.
# self deonotes the object.
# asish is a classobject or class or blueprint of Account.
# sai is a instance of Account class.
class Account:
	balance = 0   # class variable
	def deposit(self):  # method
		self.balance = self.balance + 1000
		return self.balance
	def withdraw(self):
		self.balance = self.balance - 300
		return self.balance

# sai
sai = Account() # instance  or object
print type(sai)
print dir(sai)
sai.deposit()
sai.withdraw()
print sai.balance

# asish
asish = Account
print type(asish)  # classobj or class
print dir(asish)
print asish.balance
asish.balance = 2000
print asish.balance
print sai.balance
asish.deposit()





# example 1: class variable and defination of class
#class Account(object):
class Account:
	balance = 0   # class variable


# asish
asish = Account
print type(asish)  # classobj or class
print dir(asish)
print asish.balance
asish.balance = 1000
print asish.balance

# sai
sai = Account() # instance  or object
print type(sai)
print dir(sai)
print sai.balance
'''

