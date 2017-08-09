#!/usr/bin/python
# logical operator - and
'''

task: please write a logic to resolve this issue.
khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/Batch-63$ python big.py
please enter your number1:21
please enter your number2:21
please enter your number3:11
21,11 and 21 are all equals.


'''

num1 = input("please enter your number1:")
num2 = input("please enter your number2:")
num3 = input("please enter your number3:")

if num1 > num2 and num1 > num3:
	print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num1 and num2 > num3:
	print "{1} is greater than {0} and {2}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
	print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
	print "{0},{2} and {1} are all equals.".format(num1,num2,num3)