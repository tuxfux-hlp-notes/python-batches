#!/usr/bin/python
# self - represents your object/instance
# __init__ -> special class -> constructor

# class Account(object):
class Account:  # parent class/super class
	
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

# inheritance

class MinBalAccount(Account): # child class/sub class 

	def __init__(self):  # we cannot inherit an constructor into our child class.
		Account.__init__(self)

	def withdraw(self,amount):
		self.amount = amount
		if self.balance - self.amount < 1000:
			return "Buddy!!! its time to call your daddy !!"
		else:
			Account.withdraw(self,amount)


# soumitri - employee - ready credit
soumitri = Account()
# deposited - 10000
soumitri.deposit(10000)
# balance
print soumitri.my_balance()
# withdraw - 12000
soumitri.withdraw(12000)
# balance
print soumitri.my_balance()


# kumar - student - minimum balance 1000. (5000 > max withdraw 4000)
kumar = MinBalAccount()
print dir(kumar)
# calls his daddy
kumar.deposit(5000)
print kumar.my_balance()
# withdraw
kumar.withdraw(3000)         # withdraw - Account
print kumar.my_balance()
print kumar.withdraw(2000)  # withdraw - MinBalAccount