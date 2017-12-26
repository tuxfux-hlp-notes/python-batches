#!/usr/bin/python
# function
# function closures
# @ is a decorator
#  http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# https://github.com/tuxfux-hlp/Python-examples/blob/master/devops/fabfile.py



def outer(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)
		except Exception as e:
			return "we hit on an exception {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner

# my functions
def my_add(a,b):
	return a + b

# my decorated functions.
my_add = outer(my_add)

print my_add(11,12)
print my_add(a='linux',b=' rocks')
print  my_add(11,'rocks')

'''
# use case 2:
@outer
def my_add(a,b):
	return a + b

@outer
def my_div(a,b):
	return a/b

print my_add(11,12)
print my_add(a='linux',b=' rocks')
print  my_add(11,'rocks')
print my_div(20,2)
print my_div(10,0)

# use case I:
def my_add(a,b):
	try:
		a + b
	except Exception as e:
		return "we hit on an exception {}".format(e)
	else:
		return a + b


def my_div(a,b):
	try:
		a/b
	except Exception as e:
		return "we hit on an exeption {}".format(e)
	else:
		return a/b

print my_add(11,12)
print my_add('linux','rocks')
print  my_add(11,'rocks')
print my_div(20,2)
print my_div(10,0)
'''