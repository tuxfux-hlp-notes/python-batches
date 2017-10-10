#!/usr/bin/python
# method - constructor
# inheritance

# blueprint
# class Account(object):
# class Account:
class Account:
	def __init__(self):  # constructor.
		self.balance = 0 # data
	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self,amount):
		self.balance = self.balance - amount
		return self.balance
	def bal(self):  # method
		# self denotes the instance itself
		return "my balance is {}".format(self.balance)

class MinAccount(Account):
	def __init__(self):
		Account.__init__(self)
	def withdraw(self,amount):
		if self.balance - amount < 1000:
			return "please call your daddy!!"
		else:
			Account.withdraw(self,amount)

# navya

navya = MinAccount()
navya.deposit(10000)
print "balance - {} ".format(navya.bal())
navya.withdraw(6000)
print "balance - {} ".format(navya.bal())
print navya.withdraw(3500)
print "balance - {} ".format(navya.bal())
navya.deposit(3000)
print "balance - {} ".format(navya.bal())
print navya.withdraw(6000)
print "balance - {} ".format(navya.bal())

# ansh
ansh = Account()
ansh.deposit(10000)
print "salary deposited - {} ".format(ansh.bal())
ansh.withdraw(8000)
print "balance - {} ".format(ansh.bal())
ansh.withdraw(8000)
print "balance - {} ".format(ansh.bal())