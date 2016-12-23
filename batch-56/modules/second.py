#!/usr/bin/python
import first as f

def my_add(a,b):
	'''
		this program is for addition of integers.
	'''
	a = int(a)
	b = int(b)
	return a + b

# Main
if __name__ == '__main__':
	print "addition of two numbers is {}".format(my_add(2,3))
	print "addition of two strings is {}".format(f.my_add("pine","apple"))
