#!/usr/bin/python
# HW: clear the logical issue.

'''
tcloudost@tcloudost-VirtualBox ~/Documents/git_repositories/python-batches/batch-62 $ python big.py please enter you num1:11
please enter your num2:11
please enter your num3:11
11  11 and 11 are all equals
tcloudost@tcloudost-VirtualBox ~/Documents/git_repositories/python-batches/batch-62 $ python big.py please enter you num1:39
please enter your num2:69
please enter your num3:69
39  69 and 69 are all equals
tcloudost@tcloudost-VirtualBox ~/Documents/git_repositories/python-batches/batch-62 $ python big.py please enter you num1:69
please enter your num2:39
please enter your num3:39
69 is greater than 39 and 39
tcloudost@tcloudost-VirtualBox ~/Documents/git_repositories/python-batches/batch-62 $ 

'''

num1 = input("please enter you num1:")
num2 = input("please enter your num2:")
num3 = input("please enter your num3:")

if num1 > num2 and num1 > num3:
    print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num1 and num2 > num3:
    print "{1} is greater than {0} and {2}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
    print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
    print "{0}  {1} and {2} are all equals".format(num1,num2,num3)
