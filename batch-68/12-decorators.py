#!/usr/bin/python
# function
# function closures
# @ is a decorator
#  http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# https://github.com/tuxfux-hlp/Python-examples/blob/master/devops/fabfile.py


# use case III
def outer(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)
		except Exception as e:
			return "we hit on - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner

@outer
def my_div(a,b):
	return a/b

@outer
def my_add(a,b):
	return a + b

print my_add(2,3)
print my_add(a=2,b=3)
print my_add("linux",26)
print my_div(22,11)
print my_div("ten","eleven")

'''
# use case II

def outer(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)
		except Exception as e:
			return "we hit on - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner


def my_div(a,b):
	return a/b

def my_add(a,b):
	return a + b

## how to decorate
my_add = outer(my_add)
my_div = outer(my_div)

print my_add(2,3)
print my_add(a=2,b=3)
print my_add("linux",26)
print my_div(22,11)
print my_div("ten","eleven")


## use case I
def my_div(a,b):
	try:
		a/b
	except Exception as e:
		return "we hit on - {}".format(e)
	else:
		return a/b

def my_add(a,b):
	try:
		a + b
	except Exception as e:
		return "we hit on -  {}".format(e)
	else:
		return a + b

print my_add(1,2)
print my_add("python","rocks")
print my_add("python",22)

print my_div(22,11)
print my_div("ten","eleven")
'''