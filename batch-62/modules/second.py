#!/usr/bin/python

import sys
sys.path.insert(0,'/home/tcloudost/Documents/git_repositories/python-batches/batch-62/modules/extra')

import first as f

def my_add(a,b):
	'''
		I want to add two integers.
	'''
	a = int(a)
	b = int(b)
	return a + b

# Main
if __name__ == '__main__':
	print "addition of two integers is {}".format(my_add(1,2))
	print "addition of two strings is {}".format(f.my_add("python","rocks"))