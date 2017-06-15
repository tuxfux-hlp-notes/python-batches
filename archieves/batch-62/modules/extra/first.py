#!/usr/bin/python

version = 2.0

def my_add(a,b):
	'''
		This is for addition of strings and numbers.
		syntax: my_add(a,b)
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

def my_multi(a,b):
	return a * b

def my_div(a,b=1):
	return a/b

# Main
if __name__ == '__main__':
	print "Launch a Missile."