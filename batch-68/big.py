#!/usr/bin/python

num1 = input("please enter your num1:")
num2 = input("please enter your num2:")
num3 = input("please enter your num3:")

if num1 > num2 and num1 > num3:
	print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num3 and num2 > num1:
	print "{1} is greater than {2} and {0}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
	print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
	print "{0} ,{1} and {2} are all equal".format(num1,num2,num3)

'''
## solve the logical error

khyaathi@khyaathipython:~/Documents/git_repos/python-batches/batch-68$ python big.py 
please enter your num1:21
please enter your num2:33
please enter your num3:33
21 ,33 and 33 are all equal
khyaathi@khyaathipython:~/Documents/git_repos/python-batches/batch-68$ 

'''