#!/usr/bin/python
# constructor - The first fucntion which gets implemented when you create an object.
#__ -> dunder or magic method.
# __init__ function gets called implicitly. - constructor.
# acc_bal function get called explicitly.
# Inheritance
# Account-> parent/super class
# MinAccountBalance -> child class.


# i want a minimum balance for students and not for employees.

# class Account(object
class Account:       # class/blueprint
	def __init__(self):
		self.bal = 0      # attribute
	def my_deposit(self,amount):
		self.amount = amount
		self.bal = self.bal + self.amount
		return self.bal
	def my_withdraw(self,amount):
		self.amount = amount
		self.bal = self.bal - self.amount
		return self.bal
	def my_account_bal(self):   # method
		return "balance amount {} ".format(self.bal)


class MinAccountBalance(Account):
	def __init__(self):
		Account.__init__(self)   # you cannot inherit an constructor.
	def my_withdraw(self,amount):
		self.amount = amount
		if self.bal - self.amount < 1000:
			print  "buddy!!! time to call you daddy!!!"
		else:
			Account.my_withdraw(self,amount)

# Surya - student
surya = MinAccountBalance()
print dir(surya)
surya.my_deposit(5000)
print "the amount after deposit is {}".format(surya.my_account_bal())
surya.my_withdraw(2000)
print "the amount after withdraw is {}".format(surya.my_account_bal())

# venkat - working
venkat = Account()