#!/usr/bin/python
# constructor - The first fucntion which gets implemented when you create an object.
#__ -> dunder or magic method.
# __init__ function gets called implicitly. - constructor.
# acc_bal function get called explicitly.

# class Account(object)
class Account:       # class/blueprint
	def __init__(self,amount=1000):
		self.balance = amount      # attribute
	def acc_bal(self):   # method
		return "balance amount {} ".format(self.balance)

# sujani - working

sujani = Account(amount=0)
print "balance for sujani is {}".format(sujani.acc_bal())

# rahul - student
rahul = Account()
print "balance for rahul is {}".format(rahul.acc_bal())
