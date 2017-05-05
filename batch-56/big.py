#!/usr/bin/python
# bug solving: 32,32,23

def max(a,b):
    if a>b :
        return a
    
    return b

num1 = int(raw_input("please enter your num1:"))
num2 = int(raw_input("please enter your num2:"))
num3 = int(raw_input("please enter your num3:"))

largest = max(num1,num2)
largest_final = max(largest,num3)

print "largest among the three is ",largest_final"
