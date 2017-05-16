#!/usr/bin/python
# self - represents your object/instance

# class Account(object):
class Account:
	balance = 0   # class variable
	def display_bal(self):  # method
		return "the balance is {}".format(self.balance)


# Aditya
Aditya = Account()
print type(Aditya)
print dir(Aditya)
print Aditya.balance
Aditya.balance = 1000
print Aditya.balance
print Aditya.display_bal()
'''
Traceback (most recent call last):
  File "third.py", line 17, in <module>
    print Aditya.display_bal()
TypeError: display_bal() takes no arguments (1 given)

code --
# class Account(object):
class Account:
	balance = 0
	def display_bal():
		return "the balance is {}".format(balance)
'''

# Soumitri
Soumitri = Account()
print type(Soumitri)
print dir(Soumitri)
print Soumitri.balance
Soumitri.balance = 9000
print Soumitri.balance
print Soumitri.display_bal()



print type(Account)  # <type 'classobj'> / class
print type(Account()) # <type 'instance'>/ object

# a is a class
a = Account
print type(a)  # <type 'classobj'>
print dir(a) # ['__doc__', '__module__', 'balance']
print a.balance

# b is a instance created from blue print Account.
b = Account()
print type(b) #  <type 'instance'>
print dir(b)  # ['__doc__', '__module__', 'balance']

