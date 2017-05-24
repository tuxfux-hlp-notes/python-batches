#!/usr/bin/python
# self - represents your object/instance
# __init__ -> special class -> constructor

# class Account(object):
class Account:
	
	def __init__(self):    # constructor/Get initiated automatically
		self.balance = 0   # instance variable

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

# Keerthan
Keerthan = Account
print dir(Keerthan),type(Keerthan)
Keerthan = Account()
print dir(Keerthan),type(Keerthan)

# Initial balance
print Keerthan.my_balance()
# deposit some 10000 rupess
print Keerthan.deposit(10000)
print Keerthan.my_balance()
# withdraw of amount
print Keerthan.withdraw(1000)
print Keerthan.my_balance()

# Aditya
Aditya = Account()
# initial balance
print Aditya.my_balance()
# deposit
Aditya.deposit(5000)
print Aditya.my_balance()