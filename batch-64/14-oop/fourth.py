#!/usr/bin/python
# __init__ -> constructor or speical method.
# __init__ function get called implicitly.
# other method we need to call them explicitly.
# self represents your object and it associated the variable to that object.
# but self is not a keyword, its just a variable.
class Account:
	def __init__(self):    # this method gets initiated only when you create a instance.
		self.balance = 0   # instance variable
	def deposit(self,amount):  # method
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self,amount):
		self.balance = self.balance - amount
		return self.balance
	def deposits(self):
		return "my deposits are {}".format(self.balance)

# asish
#asish = Account
#print dir(asish)  # ['__doc__', '__init__', '__module__', 'deposit', 'withdraw']

asish = Account()
print dir(asish)
asish.deposit(1000)
print asish.deposits()


##
# sai

sai = Account()
print dir(sai)
sai.deposit(2000)
print sai.deposits()
