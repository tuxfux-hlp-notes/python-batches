#!/usr/bin/python
# usage: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

# closure
def outer(my_func):
	# my_func is a local variable for outer and global for inner
	def inner(*args,**kwargs):    # in innner you are decorating the my_func passed from outer
		try:
			my_func(*args,**kwargs)
		except Exception as e:
			return "we hit on the following error - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner


@outer        # add = outer(add)
def add(a,b):
	return a + b

@outer        # div = outer(div)
def div(a,b):
	return a/b

print div(10,2) # 5
print div(10,0)
print add('linux','rocks') # args
print add(a='python',b='rocks') # kwargs
print add('linux',2)


'''
# new decorated functions
add = outer(add)
print add
print add('linux','rocks')
print add('linux',2) 

div = outer(div)
print div
print div(10,2) # 5
print div(10,0)



# use case - not an issue but can be written better
def add(a,b):
	try:
		a + b
	except Exception as e:
		return "we hit on the following error - {}".format(e)
	else:
		return a + b

def div(a,b):
	try:
		a/b
	except Exception as e:
		return "we hit on the following error - {}".format(e)
	else:
		return a/b

# Main
print div(10,2) # 5
print div(10,0)
print add('linux','rocks')
print add('linux',2)
'''

