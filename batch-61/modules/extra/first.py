#!/usr/bin/python

version = 2.0

def my_add(a,b):
	'''
		This is for addition of two numbers or strings. 
		syntax: my_add(11,22)
	'''
	return a + b

def my_sub(a,b):
	'''
		This is for substraction of two numbers.
	'''
	if a > b:
		return a - b
	else:
		return b - a

def my_div(a,b):
	'''
		This is for division of two numbers.
	'''
	return a/b

def my_multi(a,b):
	'''
		This is for multiplication of two numbers.
	'''
	return a * b

# Main
if __name__ == '__main__':
	print "Launching a missile"
	print "multiplication of two numbers {}".format(my_multi(23,33))
