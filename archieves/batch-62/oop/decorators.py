#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def outer(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)
		except Exception as e:
			return "we hit on exception - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner

# my function.

@outer
def div(a,b):
	return a/b

@outer
def add(a,b):
	return a + b


# case 1
print div(10,2) # 5
print div(5,0)

# case 2
print add(10,20)
print add(10,'linux')


'''

## old way calling decorators

# my function.
def div(a,b):
	return a/b

def add(a,b):
	return a + b

new_div = outer(div)
print new_div(10,2)
print new_div(5,0)

new_add = outer(add)
print new_add(10,20)
print new_add(10,'linux')


##
# what we do.. always.
##

def div(a,b):
	try:
		a/b
	except Exception as e:
		return "we hit on exception - {}".format(e)
	else:
		return a/b

def add(a,b):
	try:
		a + b
	except Exception as e:
		return "we hit on  exeption - {}".format(e)
	else:
		return a + b


# case 1
print div(10,2) # 5
print div(5,0)

# case 2
print add(10,20)
print add(10,'linux')

'''