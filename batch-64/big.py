#!/usr/bin/python

num1 = int(raw_input("please enter the num1:"))
num2 = int(raw_input("please enter the num2:"))
num3 = int(raw_input("please enter the num3:"))

if  num1 > num2 and num1 > num3:
	print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num3 and num2 > num1:
	print "{1} is greater than {2} and {0}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
	print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
	print "{},{} and {} are all equal".format(num1,num2,num3)

'''
# correct this.
khyaathi@khyaathipython:~/Documents/git_repos/python-batches/batch-64$ python big.py
please enter the num1:22
please enter the num2:22
please enter the num3:11
22,22 and 11 are all equal
khyaathi@khyaathipython:~/Documents/git_repos/python-batches/batch-64$ 



'''