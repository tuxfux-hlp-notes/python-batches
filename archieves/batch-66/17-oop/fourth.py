#!/usr/bin/python
# __init__ is  a constructor is a special method.
# This method gets initiated only when you create an instance.

class Account:
	def __init__(self):   # constructor.
		self.balance = 0  # instance variable/data
	def my_deposit(self):
		self.balance = self.balance + 1000
		return self.balance
	def my_withdraw(self):
		self.balance = self.balance - 200
		return self.balance
	def my_balance(self):  # method
		return "my balance is {}".format(self.balance)  # self.balance -> instance variable.


# class
A = Account
print dir(A)

# soujanya
sowji = Account()  # instance
print dir(sowji)
sowji.my_deposit()
sowji.my_deposit()
print sowji.my_balance()

# muyuri
mayuri = Account()  # instance
print dir(mayuri)
mayuri.my_deposit()
print mayuri.my_balance()