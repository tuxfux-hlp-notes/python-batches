#!/usr/bin/python

import sys
# from first import my_add  - wrong way of importing in this case. 
sys.path.insert(0,'/home/key2gyaan/Documents/git_repositories/tuxfux-hlp-notes/batch-57/modules/extra')
import first as f

def my_add(a,b):
	''' this function is for addition of integers '''
	a = int(a) 
	b = int(b)
	return a + b

# main
print "this is for addition of numbers and strings."
print "addition of two numbers is {}".format(my_add(20,21))
print "addition of two string is {}".format(f.my_add("linux"," rocks"))