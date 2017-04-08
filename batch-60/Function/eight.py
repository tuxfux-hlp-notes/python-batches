#!/usr/bin/python
# *,**,*args,**kwargs

# *
def my_add(a,b):
	return a + b

# list
my_list = [22,33]
my_list1 = [22,33,44]


# **
# dictionary
my_value = {'b':55,'a':22}
my_value1 = {'c':55,'a':33}

# a = my_list[0]
# b = my_list[1]
# print my_add(a,b)

# when using a list use * .
print my_add(*my_list)   # output
#print my_add(*my_list1)  # error

# when using a dictionary use **.
print my_add(**my_value)
print my_add(**my_value1)