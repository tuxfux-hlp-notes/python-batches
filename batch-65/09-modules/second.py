#!/usr/bin/python


# /home/khyaathi/Documents/git_repos/python-batches/batch-65 
# automate the above path
# hint : os module
import sys
sys.path.insert(0,'/home/khyaathi/Documents/git_repos/python-batches/batch-65/modules/extra')
import first as f

def my_add(a,b):
	''' this is for addition of number '''
	a = int(a)
	b = int(b)
	return a + b

if __name__ == '__main__':
	print "the addition of two numbers is {}".format(my_add(1,2))
	print "the addition of two string is {}".format(f.my_add('linux','rocks'))