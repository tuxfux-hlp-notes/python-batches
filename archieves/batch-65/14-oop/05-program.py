#!/usr/bin/python
# method - constructor

# blueprint
# class Account(object):
# class Account:
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

# kumar
kumar = Account()
print dir(kumar)
kumar.deposit()
print kumar.amount()
kumar.withdraw()
print kumar.amount()

# dhar
dhar = Account()
print dhar.amount()