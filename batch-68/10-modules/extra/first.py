#!/usr/bin/python

version = 2.0

def my_add(a,b):
	'''    
		this is adding numbers and strings.
	'''
	return a + b

def my_sub(a,b):
	'''
		this is for substracting a smaller number with a larger number.
	'''
	if a > b:
		return a - b
	else:
		return b - a

def my_multi(a,b):
	'''
		Multiplication of two numbers.
	'''
	return a * b

def my_div(a,b=1):
	'''
		division of two numbers.
	'''
	return a/b

# main
if __name__ == '__main__':
	print "Launching a missile."