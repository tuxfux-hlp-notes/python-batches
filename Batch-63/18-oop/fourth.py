#!/usr/bin/python
# __init__ -> special method is called as constructor.
# this get initiated automatically.

#class Account(object):

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

# kaushik - instance/object
kaushik = Account()
kaushik.my_deposit(10000)
print "The amount with kaushik after deposit - {}".format(kaushik.my_balance())
kaushik.my_withdraw(3000)
print "The amount with kaushik after withdraw - {}".format(kaushik.my_balance())


# mahesh - instance/object
mahesh = Account()
print "Initial amount of mahesh {}".format(mahesh.my_balance())
mahesh.my_deposit(5000)
print "The amount with mahesh after deposit - {}".format(mahesh.my_balance())
mahesh.my_withdraw(3000)
print "The amount with mahesh after withdraw - {}".format(mahesh.my_balance())
