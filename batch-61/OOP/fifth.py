#!/usr/bin/python
# self - represents your object/instance
# __init__ -> special class -> constructor

# class Account(object):
class Account:
	
	def __init__(self,amount=0):    # constructor/Get initiated automatically
		self.balance = amount  # instance variable


	def deposit(self,amount):
		self.amount = amount
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self,amount):
		self.amount = amount
		self.balance = self.balance - amount
		return self.balance

	def my_balance(self):  # method
		return "the balance is {}".format(self.balance)


# soumitri - working - zero balance account.
soumitri = Account()  # instance
# initial balance
print soumitri.my_balance()


# kumar - student - mim balance account
kumar = Account(amount=1000) # instance
# initial balance
print kumar.my_balance()