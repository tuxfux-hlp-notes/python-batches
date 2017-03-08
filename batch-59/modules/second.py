#!/usr/bin/python

import sys
sys.path.insert(0,'/home/tcloudost/Documents/git_repositories/python-batches/batch-59/modules/extra')

import first as g

def my_add(a,b):
	''' Addtion of only float values '''
	a = float(a)
	b = float(b)
	return a + b

# Main
if __name__ == '__main__':
	print "addition of two floats is {}".format(my_add(11,22))
	print "addition of two string is {}".format(g.my_add('python','django'))