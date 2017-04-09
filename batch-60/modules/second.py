#!/usr/bin/python

import sys
sys.path.insert(0,'/home/tcloudost/Documents/git_repositories/python-batches/batch-60/modules/extra')
import first

def my_add(a,b):
	''' this is only for addition of integers '''
	a = int(a)
	b = int(b)
	result = a + b
	return result


if __name__ == '__main__':
	print "addition of two numbers {}".format(my_add(10,22))
	print "addition of two strings {}".format(first.my_add("linux","rocks"))
