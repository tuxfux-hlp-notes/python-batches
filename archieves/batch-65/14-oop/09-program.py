#!/usr/bin/python
# http://radek.io/2011/07/21/private-protected-and-public-in-python/
class Account:
	def __init__(self):  # constructor - get called implicitly.
		self.balance = 0 # data
	def deposit(self):
		self.balance = self.balance + 1000
		return self.balance
	def withdraw(self):
		self.balance = self.balance - 200
		return self.balance
	def amount(self):  # method
		# self denotes the instance itself
		return "my balance is {}".format(self.balance)

# sridhar
sridhar = Account()
sridhar.balance = 2000
print sridhar.amount()
