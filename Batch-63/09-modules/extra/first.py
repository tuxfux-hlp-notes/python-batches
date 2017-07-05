#!/usr/bin/python
# usage: my first python program.

version = 2.0

def my_add(a,b):
	'''
		This is for addition of numbers and strings
		syntax: my_add(a,b) 
	'''
	return a + b

def my_sub(a,b):
	'''
		This is for substration of two numbers.
		substracting a smaller number from a larger number.
	'''

	if a > b:
		return a - b
	else:
		return b - a

def my_multi(a,b):
	return a * b

def my_div(a,b=1):
	return a/b


# Main

if __name__ == '__main__': # anything below this line will not be imported.
	print "Launching a Missile"