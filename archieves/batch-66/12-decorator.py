#!/usr/bin/python
# decorators
# # http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def upper(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)  # my_add(10,20)
		except Exception as e:
			return "The error  is - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner

def my_add(a,b):
	return a + b
# how @ is workiing in backend.. for python version < 2.4
print type(my_add)
print my_add
my_add = upper(my_add)
print my_add

print my_add(10,20) ## **args comes into actions.
print my_add(a=10,b=30) ## **kwargs comes into actions.
print my_add('hello',30)

'''
# use case II
def upper(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)
		except Exception as e:
			return "The error  is - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner

@upper
def my_add(a,b):
	return a + b

@upper
def my_div(a,b):
	return a/b

print my_add(10,20)
print my_add('hello',30)
print my_div(10,5)
print my_div(10,0)


# use case I
def my_div(a,b):
	try:
		a/b
	except  Exception as e:
		return "The error  is - {}".format(e)
	else:
		return a/b 


def my_add(a,b):
	try:
		a + b
	except  Exception as e:
		return "The error  is - {}".format(e)
	else:
		return a + b

# main
print my_add(10,20)
print my_add('hello',30)
print my_div(10,5)
print my_div(10,0)
'''