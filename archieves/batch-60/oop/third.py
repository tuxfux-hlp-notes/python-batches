#!/usr/bin/python

# class Account(object)
class Account:       # class/blueprint
	balance = 0      # attribute
	def acc_bal(self):   # method
		return "balance amount {} ".format(self.balance)


print Account,type(Account)  # __main__.Account,<type 'classobj'> / class(other languages)
print type(Account())        # <type 'instance'> / object(other languages)

# Ramya
ramya = Account()
print type(ramya),dir(ramya)
print ramya.balance
ramya.balance = 1000
print ramya.balance

# sujani
sujani = Account()
print sujani.balance
print dir(sujani)
print sujani.acc_bal()
'''
Traceback (most recent call last):
  File "third.py", line 24, in <module>
    print sujani.acc_bal()
TypeError: acc_bal() takes no arguments (1 given)
'''

# ramya balance
print ramya.acc_bal()
