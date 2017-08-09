#!/usr/bin/python
# __init__ -> special method is called as constructor.
# this get initiated automatically.

#class Account(object):

class Account:
	def __init__(self):
		self.balance = 0
	def deposit(self):   # self denoted the object itself.
		return self.balance


# Mahesh
'''
mahesh = Account
print dir(mahesh) # __doc__', '__init__', '__module__', 'deposit'] 
# balance is no longer a class variables its a instance variable.
'''
mahesh = Account()
print dir(mahesh)
print "Mahesh initial balance is {}".format(mahesh.balance)
print "My balance amount is {}".format(mahesh.deposit())

'''
--- we are getting this issue when we have the self not presnet for deposit account.
	def deposit():   # self denoted the object itself.
		print "the balance amount is {}".format(self.balance)

print "My balance amount is {}".format(mahesh.deposit())
Traceback (most recent call last):
  File "third.py", line 22, in <module>
    print "My balance amount is {}".format(mahesh.deposit())
TypeError: deposit() takes no arguments (1 given)
'''


## kaushik
kaushik = Account()
print dir(kaushik)
kaushik.balance = 100
print "Kaushik initial balance is {}".format(kaushik.balance)
print "My balance amount is {}".format(kaushik.deposit())


'''
# example 1

class Account:
	balance = 0  # class variable


print Account,type(Account) # __main__.Account,<type 'classobj'>/class
print Account(),type(Account()) # <__main__.Account instance at 0x7fa6df90f3f8> <type 'instance'>/object

# Mahesh
mahesh = Account
print dir(mahesh) # ['__doc__', '__module__', 'balance'] # balance is a class variable
'''

