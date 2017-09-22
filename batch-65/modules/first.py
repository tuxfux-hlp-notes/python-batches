#!/usr/bin/python

version=2

def my_add(a,b):
	''' This function is for addition of numbers and string '''
	return a + b

def my_sub(a,b):
	''' This function is for substraction of numbers'''
	if a > b:
		return a - b
	else:
		return b - a

def my_multi(a,b):
	''' This is for multiplication of two numbers '''
	return a * b

def my_div(a,b):
	''' This is for division of two numbers '''
	return a/b


# main
if __name__ == '__main__':  # all the lines below this wont be imported.
	print "Launch a missile."