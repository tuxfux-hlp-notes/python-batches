#!/usr/bin/python

#class Account(object):
class Account():
	balance = 0 # class variable
	def my_bal(self): # method
		return "my balance amount is {}".format(self.balance)

print Account        # __main__.Account
print type(Account)  # <type 'classobj'> / class
print Account()      # <__main__.Account instance at 0x7fd72be3c830>
print type(Account()) # <type 'instance'>/ object

# Abhi
abhi = Account
print dir(abhi)
print abhi.balance
abhi.balance = 1000
print abhi.balance
#print abhi.my_bal()
'''
Traceback (most recent call last):
  File "third.py", line 20, in <module>
    print abhi.my_bal()
TypeError: unbound method my_bal() must be called with Account instance as first argument (got nothing instead)
'''
abhi = Account()
print abhi.balance # 1000
print abhi.my_bal()
'''
Traceback (most recent call last):
  File "third.py", line 29, in <module>
    print abhi.my_bal()
TypeError: my_bal() takes no arguments (1 given)

# after adding self to my_bal(self)
Traceback (most recent call last):
  File "third.py", line 29, in <module>
    print abhi.my_bal()
  File "third.py", line 7, in my_bal
    return "my balance amount is {}".format(balance)
NameError: global name 'balance' is not defined


'''


# Vishwa
vishwa = Account()
vishwa.balance = 0
print vishwa.balance
print vishwa.my_bal()