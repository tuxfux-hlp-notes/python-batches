#!/usr/bin/python
# local variable/namespaces and global variables/namespaces
# variables defined inside a function are called as local variables.
# a variable defined within a function is available during the run time of the function.
# once your function is run the variable inside the function is no longer available.

def my_value():
	x = 1
	print locals() # {'x': 1}
	return x

print my_value() # 1,not 1
print locals()  # {'my_value': <function my_value at 0x7f99e668c5f0>, '__builtins__': <module '__builtin__' (built-in)>,
				# '__file__': 'third.py',
				# '__package__': None, '__name__': '__main__', '__doc__': None}
print x  # no output,random number,None,not 1
         # NameError: name 'x' is not defined
