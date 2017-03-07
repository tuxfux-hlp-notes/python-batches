#!/usr/bin/python

version = 2.0

def my_add(a,b):
	''' This is for addition of strings and numbers.'''
	sum = a + b
	return sum

def my_sub(a,b):
	''' This is for substraction of two numbers'''
	if a > b:
		return a - b
	elif b > a:
		return b - a

def my_div(a,b=1):
	''' This is for division of tow numbers '''
	return a/b

def my_multi(a,b):
	''' this is for multiplication of numbers '''
	return a * b


# Main
if __name__ == '__main__':   # anything below this line wont get imported.
	print "Deposit 1000 rupees in account"