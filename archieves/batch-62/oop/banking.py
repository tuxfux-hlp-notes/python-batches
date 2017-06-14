#!/usr/bin/python
# __init__ - constructor method
# __init__ get called implicitly, or during creation of an instance.

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

# varun
varun = Account  # varun is not a instance here.
'''
print dir(varun) 
['__doc__', '__init__', '__module__', 'deposit', 'my_balance', 'withdraw']

'''
print dir(varun)
#print varun.my_balance()
'''
Traceback (most recent call last):
  File "banking.py", line 19, in <module>
    print varun.my_balance()
TypeError: unbound method my_balance() must be called with Account instance as first argument (got nothing instead)
'''

# vishwa
vishwa = Account()
print dir(vishwa)
vishwa.deposit(1000)
print vishwa.my_balance()
vishwa.withdraw(300)
print vishwa.my_balance()