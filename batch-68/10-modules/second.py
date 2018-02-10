#!/usr/bin/python
import sys
sys.path.insert(0,'/home/khyaathi/Documents/git_repos/python-batches/batch-68/10-modules/extra')
import first as f

def my_add(a,b):
	''' This is going to add two integers '''
	a = int(a)
	b = int(b)
	return a + b

if __name__ == '__main__':
	print "addition of two numbers is {}".format(my_add(11,12))
	print "addition of two string is {}".format(f.my_add("linux","rocks"))