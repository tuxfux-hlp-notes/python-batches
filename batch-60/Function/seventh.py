#!/usr/bin/python
# passing arguments to a function.
# positional function parametrs/arguments

def my_add(a,b):
	print locals()
	return a + b

# passing arguments based on positon.
print my_add('python','rocks')
print my_add('rocks','python')

# passing arguments based on keys.
print my_add(b='rocks',a='python')

# default function arguments


def my_multi(num,default=10):  # default is not a keywork its a variable.
	for value in range(1,default+1):
		print "{0:2d} * {1:2d} = {2:3d}".format(num,value,num*value)

my_multi(2)    # default = 10
my_multi(3,5)  # here default=5
