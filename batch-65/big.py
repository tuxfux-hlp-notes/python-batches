#!/usr/bin/python
num1 = input("please enter your num1:")
num2 = input("please enter your num2:")
num3 = input("please enter your num3:")

if num1 > num2 and num1 > num3:
	print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num1 and num2 > num3:
	print "{1} is greater than {2} and {0}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
	print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
	print "{0} {1} and {2} are all equals".format(num1,num2,num3)

'''
# task
root@khyaathipython:~/Documents/git_repos/python-batches/batch-65# python big.py 
please enter your num1:21
please enter your num2:21
please enter your num3:1
21 21 and 1 are all equals
root@khyaathipython:~/Documents/git_repos/python-batches/batch-65# 
'''