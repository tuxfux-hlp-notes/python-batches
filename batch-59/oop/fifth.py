#!/usr/bin/python


# Defining a class in pytohn.
#class account(object):
#class account:

'''
In [1]: class A:
   ...:     hand="lefty"
   ...:     work="singer"
   ...:     

In [2]: class B:
   ...:     hand="right"
   ...:     work="doctor"
   ...:     

In [3]: class C(A,B):
   ...:     pass
   ...: 

In [4]: Abhi=C()

In [5]: print dir(Abhi)
['__doc__', '__module__', 'hand', 'work']

In [6]: Abhi.hand
Out[6]: 'lefty'

In [7]: Abhi.work
Out[7]: 'singer'
'''

# inheritance

class account:      # <type 'classobj'>/class
	def __init__(self):      # constructor
		self.balance = 0     # class schema variable.
	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self,amount):
		self.balance = self.balance - amount
		return self.balance
	def final(self):
		return "my initial balance is {}".format(self.balance)

class MinBalAccount(account):
	def __init__(self):
		account.__init__(self)
	def withdraw(self,amount):
		if self.balance - amount < 1000:
			return "buddy!! its time to call your daddy."
		else:
			return account.withdraw(self,amount)

print "# Vinod"
Vinod = MinBalAccount()
print "my initial balance {}".format(Vinod.balance)
Vinod.deposit(5000)
print "my balance after deposit {}".format(Vinod.balance)
Vinod.withdraw(3000)
print "my balance after withdraw {}".format(Vinod.balance)
print Vinod.withdraw(1500)
print "my balance after withdraw {}".format(Vinod.balance)
print Vinod.withdraw(1000)
print "my balance after withdraw {}".format(Vinod.balance)
# print "my balance after deposit {}".format(Hemant.balance)


print "# Hemant"
Hemant = account()
print "my initial balance {}".format(Hemant.balance)
Hemant.deposit(5000)
print "my balance after deposit {}".format(Hemant.balance)
Hemant.withdraw(10000)
print "my balance after deposit {}".format(Hemant.balance)




