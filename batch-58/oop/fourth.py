#!/usr/bin/python


# Defining a class in pytohn.
#class account(object):
#class account:

class account:      # <type 'classobj'>/class
	def __init__(self,bal):      # constructor
		self.balance = bal     # class schema variable.
	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self,amount):
		self.balance = self.balance - amount
		return self.balance
	def final(self):
		return "my initial balance is {}".format(self.balance)

# constructor - __init__ -> is called implicitly.
# deposit,withdraw,final -> explictly need to be called.

# vinod - student
# sbi
vinod = account(1000)
print vinod.final()

# Hemant - professional
hemant = account(0)
print hemant.final()


