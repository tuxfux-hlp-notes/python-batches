#!/usr/bin/python
# __init__ - constructor method
# __init__ get called implicitly, or during creation of an instance.

# super class
# parent class
class Account():
	def __init__(self):  # construtor
		self.balance = 0 # class variable
	def deposit(self,amount): # method
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self,amount): # method
		self.balance = self.balance - amount
		return self.balance	
	def my_balance(self):
		return "my balance amount is {}".format(self.balance)

# sub class
# child class
class MinAccount(Account):
	def __init__(self):
		Account.__init__(self)
	def withdraw(self,amount):
		if self.balance - amount < 1000:
			print "Please call your daddy!!"
		else:
			Account.withdraw(self,amount)

# working
# viraja

viraja = Account()
# salary day
viraja.deposit(10000)
print viraja.my_balance()
viraja.withdraw(15000)
print viraja.my_balance()

# student
# deepthi
deepthi=MinAccount()
print dir(deepthi)
deepthi.deposit(5000)
print deepthi.my_balance()
deepthi.withdraw(3000)
print deepthi.my_balance()
deepthi.withdraw(2000)
deepthi.withdraw(1000)
print deepthi.my_balance()