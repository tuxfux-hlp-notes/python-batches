#!/usr/bin/python

version = 2

def my_add(a,b):
	'''
		This function is for addition of numbers and strings.
	'''
	return a + b

def my_sub(a,b):
	'''
		This is for substration from larger to smaller number.
	'''
	if a > b:
		return a - b
	else:
		return b - a

def my_div(a,b):
	return a/b

def my_multi(a,b):
	return a * b


# Main
if __name__ == '__main__':
	print "pushing some 1000 rs."