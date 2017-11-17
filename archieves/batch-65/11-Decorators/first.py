#!/usr/bin/python
# decorator - @ - function closures
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

# decorated function
def outer(my_func):
	def inner(*args,**kwargs):
		try:
			my_func(*args,**kwargs)
		except Exception as e:  # e is an instance of the Exception class.
			return "we hit on the following error - {}".format(e)
		else:
			return my_func(*args,**kwargs)
	return inner

# Main
@outer
def my_add(a,b):
	return a + b

@outer
def my_sub(a,b):
	return a - b

@outer
def my_div(a,b):
	return a/b

if __name__ == '__main__':

	print my_add,type(my_add)
	print my_add(1,2)
	print my_add("linux"," rocks")
	print my_add(1,"rocks")

	print my_sub,type(my_add)
	print my_sub(10,2)
	print my_sub("linux","rocks")

	print my_div,type(my_add)
	print my_div(10,2)
	print my_div(b=2,a=10)
	print my_div(10,0)



'''

# use case II

# old style of decoration
my_add = outer(my_add)

print my_add(1,2)
print my_add("linux"," rocks")
print my_add(1,"rocks")

my_sub = outer(my_sub)
print my_sub(10,2)
print my_sub("linux","rocks")


# use case I

def my_sub(a,b):
	try:
		a - b
	except Exception as e:
		return "we hit on the following error - {}".format(e)
	else:
		return a - b

def my_add(a,b):
	try:
		a + b
	except Exception as e:
		return "we hit on the following error - {}".format(e)
	else:
		return a + b

print my_add(1,2)
print my_add("linux"," rocks")
print my_add(1,"rocks")

print my_sub(10,2)
print my_sub("linux","rocks")
'''