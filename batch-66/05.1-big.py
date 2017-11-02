#!/usr/bin/python

num1 = input("please enter your num1:")
num2 = input("please enter your num2:")
num3 = input("please enter your num3:")

if num1 > num2 and num1 > num3:
	print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num1 and num2 > num3:
	print "{1} is greater than {0} and {2}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
	print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
	print "{0} , {1} and {2} all are equals".format(num1,num2,num3)

'''
# homework
khyaathi@khyaathipython:~/Documents/git_repos/python-batches/batch-66$ python big.py 
please enter your num1:12
please enter your num2:11
please enter your num3:12
12 , 11 and 12 all are equals
khyaathi@khyaathipython:~/Documents/git_repos/python-batches/batch-66$ 

'''