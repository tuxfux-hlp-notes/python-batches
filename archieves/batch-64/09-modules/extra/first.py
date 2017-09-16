#!/usr/bin/python

version = 3.0

def my_add(a,b):
	''' Addition of two number or strings '''
	sum = a + b
	return sum

def my_sub(a,b):
	""" Sub smaller number to larger"""
	if a > b :
		diff = a - b
	else:
		diff = b - a
	return diff

def my_div(a,b=1):
	""" divison of two numbers """
	return a/b

def my_multi(a,b):
	''' multiplication of wto numbers '''
	return a * b

# Main
if __name__ == '__main__':
	print "launching a missile."
