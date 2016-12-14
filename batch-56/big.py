#!/usr/bin/python
# bug solving: 32,32,23
num1 = int(raw_input("please enter your num1:"))
num2 = int(raw_input("please enter your num2:"))
num3 = int(raw_input("please enter your num3:"))

if num1 > num2 and num1 > num3:
    print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num1 and num2 > num3:
    print "{1} is greater than {0} and {2}".format(num1,num2,num3)
elif num3 > num1 and num3 > num2:
    print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
    print "{0}, {1} and {2} are all equal".format(num1,num2,num3)
