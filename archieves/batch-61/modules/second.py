#!/usr/bin/python

import sys
sys.path.insert(0,'/home/tcloudost/Documents/git_repositories/python-batches/batch-61/modules/extra')

import first as f

def my_add(a,b):
	'''
		this is for addition of numbers.
	'''
	a = int(a)
	b = int(b)
	return a + b

print "addition of two numbers is {}".format(my_add(10,12))
print "addition of two strings is {}".format(f.my_add("linux"," rocks"))