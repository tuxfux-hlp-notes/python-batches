#!/usr/bin/python
# __init__ is  a constructor is a special method.
# This method gets initiated only when you create an instance.

# Super class/parent class
class Account:
	def __init__(self):   # constructor.
		self.balance = 0  # instance variable/data
	def my_deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance
	def my_withdraw(self,amount):
		self.balance = self.balance - amount
		return self.balance
	def my_balance(self):  # method
		return "my balance is {}".format(self.balance)  # self.balance -> instance variable.

# Sub class/child class
class MinBalAccount(Account):    # Account is the parent class,MinBalAccount is child class.
	def __init__(self):
		Account.__init__(self)   # we are importing all variables from parent class.
	def my_withdraw(self,amount):
		if self.balance - amount < 1000:
			return "Time to call your daddy!!"
		else:
			return Account.my_withdraw(self,amount)

##
#  employees,non-employees
##

# mahendra
# salaried - overdraft.

mahi = Account()
mahi.my_deposit(10000)
print mahi.my_balance()
mahi.my_withdraw(2500)
print mahi.my_balance()
mahi.my_withdraw(2500)
print mahi.my_balance()
mahi.my_withdraw(6000)
print mahi.my_balance()

# mreddy
# minimum balance of 1000

print "-" * 20
mreddy = MinBalAccount()
mreddy.my_deposit(6000)  # 1000 is mim balance + 5000 is for monthly expenditure
print mreddy.my_balance()
mreddy.my_withdraw(3000)
print  mreddy.my_balance()
print mreddy.my_withdraw(3000)
print mreddy.my_withdraw(2000)
print  mreddy.my_balance()
