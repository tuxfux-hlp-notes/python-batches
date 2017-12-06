#!/usr/bin/python
# using modules we are not worried about other programs namespaces.

import sys
sys.path.insert(0,'/home/khyaathi/Documents/git_repos/python-batches/batch-66/10-modules/extra')

import first as f

def my_add(a,b):
	''' This is for adding numbers only '''
	a = int(a)
	b = int(b)
	return a + b

# Main
if __name__ == '__main__':
	print "addition of two numbers is {}".format(my_add(11,22))
	print "addition of two strings is {}".format(f.my_add("linux"," rocks"))