#!/usr/bin/python

import first as f

def my_add(a,b):
	''' this is for addition of two integers '''
	a = int(a)
	b = int(b)
	return a + b

if __name__ == '__main__':
	print "addition of two integers is {}".format(my_add(11,22))
	print "addition of two string is {}".format(f.my_add('linux','rocks'))