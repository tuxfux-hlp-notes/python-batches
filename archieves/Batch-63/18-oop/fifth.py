#!/usr/bin/python
# Inheritance - Account is a parent/super class
#             - MinBalanceAccount - child/sub class
# Zero balance account opening.

class Account:            # class/classobject/blueprint
	def __init__(self):             # special method - constructor
		self.balance = 0  # data
	def my_deposit(self,amount):    # method
		self.balance = self.balance + amount
		return self.balance
	def my_withdraw(self,amount):
		self.balance  = self.balance - amount
		return self.balance
	def my_balance(self):   # self denoted the object itself.
		return self.balance

# minimum balance account - 1000 rupees to be there in my account.

class MinBalanceAccount(Account):
	def __init__(self):
		Account.__init__(self)
	def my_withdraw(self,amount):
		if self.balance - amount < 1000:
			print "Buddy!!! you dont have enough balance to withdraw"
		else:
			Account.my_withdraw(self,amount)

# Working person - overdraft to the working people.
# mahesh - instance/object
mahesh = Account()
print "Initial amount of mahesh {}".format(mahesh.my_balance())
mahesh.my_deposit(10000)
print "The amount with mahesh after deposit - {}".format(mahesh.my_balance())
mahesh.my_withdraw(8000)
print "The amount with mahesh after withdraw - {}".format(mahesh.my_balance())
mahesh.my_withdraw(5000)
print "The amount with mahesh after withdraw - {}".format(mahesh.my_balance())

# Nikhil - student
nikhil = MinBalanceAccount()
print "Initial amount of nikhil {}".format(nikhil.my_balance())
nikhil.my_deposit(5000)
print "The amount with nikhil after deposit - {}".format(nikhil.my_balance())
nikhil.my_withdraw(3000)
print "The amount with nikhil after withdraw - {}".format(nikhil.my_balance())
nikhil.my_withdraw(5000)
print "The amount with mahesh after withdraw - {}".format(nikhil.my_balance())
nikhil.my_withdraw(1000)
print "The amount with mahesh after withdraw - {}".format(nikhil.my_balance())
