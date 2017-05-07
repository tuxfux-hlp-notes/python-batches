#!/usr/bin/python
num1 = input("please enter your number1:")
num2 = input("please enter your number2:")
num3 = input("please enter your number3:")

if num1 > num2 and num1 > num3:
    print "{0} is greater than {1} and {2}".format(num1,num2,num3)
elif num2 > num3 and num2 > num1:
    print "{1} is greater than {0} and {2}".format(num1,num2,num3)
elif num3 > num2 and num3 > num1:
    print "{2} is greater than {1} and {0}".format(num1,num2,num3)
else:
    print "{1},{2},{0} are all equal".format(num1,num2,num3)   
