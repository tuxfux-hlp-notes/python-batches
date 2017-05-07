#!/usr/bin/python
# local variable/namespaces and global variables/namespaces
# variables defined inside a function are called as local variables.
# a variable defined within a function is available during the run time of the function.
# once your function is run the variable inside the function is no longer available.
# scope resolution, if local variable is not available go for global namespace.
# local namespace is given higher precedence than global namespace.

balance=0

def deposit():
	global balance
	print locals()
	balance = balance + 1000
	return balance

def withdraw():
	global balance
	print locals()
	balance = balance - 300
	return balance


print "my initial balance : {}".format(balance)
print deposit()
print "my balance after deposit: {}".format(balance)
print withdraw()
print "my balance after withdraw: {}".format(balance)