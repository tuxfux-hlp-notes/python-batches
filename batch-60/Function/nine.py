#!/usr/bin/python
# *args

# max - inbuild function
print max(2,4)
print max(2,4,6,17,-1)
print max(-1,-2,-3,-4)

# gmax  - user defined function.
def gmax(*args):
	big = -1
	for value in args:   # args provides tuple.
		if value > big:
			big = value
	return big


print gmax(2,4)
print gmax(2,4,6,17,-1)
print gmax(-1,-2,-3,-4)

