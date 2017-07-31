#!/usr/bin/python
# modules gives us benefit of working about namespace issues.

import sys
sys.path.insert(0,'/home/khyaathi/Documents/git_repos/python-batches/Batch-63/09-modules/extra')

import first as f

def  my_add(a,b):
	''' this is just for addition of integers'''
	a = int(a)
	b = int(b)
	return a + b

# Main
if __name__ == '__main__':
	print "addition of two integers is {}".format(my_add(11,22))
	print "addtion of two string is {}".format(f.my_add("linux","rocks"))