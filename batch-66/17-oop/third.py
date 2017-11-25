#!/usr/bin/python
# define class,method,instance,class variables,instance variables.
'''
# use case 1:
class Account:
	balance = 0  # class variable.

print Account          # __main__.Account
print type(Account)    # <type 'classobj'>
print Account()        # <__main__.Account instance at 0x7f27565c83f8>
print type(Account())  # <type 'instance'>



# use case 2:
# class Account(object):
# 	balance = 0  # class variable.

# print Account          # __main__.Account
# print type(Account)    # <type 'classobj'>
# print Account()        # <__main__.Account instance at 0x7f27565c83f8>
# print type(Account())  # <type 'instance'>


## understaing class and instance variables.

A = Account
print A,type(A),dir(A)
print A.balance

AI = Account()
print AI,type(AI),dir(AI)
print AI.balance

A.balance = 100
print A.balance
print AI.balance

'''
# use case 3:

class Account:
	balance = 0
	def my_balance(self):  # method
		return "my balance is {}".format(self.balance)  # self.balance -> instance variable.


# saleem
saleem = Account()
print saleem,type(saleem),dir(saleem)
print saleem.balance
print saleem.my_balance()
saleem.balance = 10000
print saleem.my_balance()


# navya

navya=Account()
print navya,type(navya),dir(navya)
print navya.balance
print navya.my_balance()


# instance vs class
print saleem.balance  # instance variables
print navya.balance   # instance variables
navya.balance = 2000
print navya.balance
print saleem.balance  # instance variables
print Account.balance # class variables
Account.balance = 1000

# soujanya
soujanya = Account()
print soujanya.balance
