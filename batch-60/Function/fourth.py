#!/usr/bin/python
# local variable/namespaces and global variables/namespaces
# variables defined inside a function are called as local variables.
# a variable defined within a function is available during the run time of the function.
# once your function is run the variable inside the function is no longer available.
# scope resolution, if local variable is not available go for global namespace.

x = 10  # global


def my_value():
	print locals() 
	return x

print globals()
print my_value() # 10
print locals()  
print x          # 10