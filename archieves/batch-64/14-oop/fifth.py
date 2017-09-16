#!/usr/bin/python
# __init__ -> constructor or speical method.
# __init__ function get called implicitly.
# other method we need to call them explicitly.
# self represents your object and it associated the variable to that object.
# but self is not a keyword, its just a variable.
# TODO - loading class as a constructor.

# inheritance
# Requirement : we need two account.
# 1. Minimum balancce account  - 1000 rs
# 2. Salary account - 0 balance.
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

class MinBalAccount(Account):   # MinBalAccount(child),Account(parent)
	def __init__(self):
		Account.__init__(self)  # get me all the variables of Account class into my MinBalAccount
	def withdraw(self,amount):
		if self.balance - amount <= 1000:
			print "Hey buddy!! time to call your daddy."
		else:
			Account.withdraw(self,amount)


# MinBalAcccount class inherited - deposit,deposits,withdraw
# withdraw function is polymorphic - Account,MinBalAccount
# Ramu.deposit(10000) is actually looking for deposit first in its own class,
# later looks into the parent class depending on order in the defination.
# for ex: MinBalAccount(Account,account1)
# first we will look into the Account class, later we will look into the account1 class.


# Main
# Ujwal - salaried
Ujwal = Account()
Ujwal.deposit(50000)
print Ujwal.deposits()
Ujwal.withdraw(70000)
print Ujwal.deposits()

# Ramu - student
Ramu = MinBalAccount()
Ramu.deposit(10000)
print Ramu.deposits()
Ramu.withdraw(8000)
print Ramu.deposits()
Ramu.withdraw(1500)
print Ramu.deposits()


# 