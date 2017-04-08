#!/usr/bin/python
# **kwargs
# logging.basicConfig?
# call-center

def callme(**kwargs):
	#for key in kwargs:      # kwargs is a dictionary.
		if 'name' in kwargs:
			print "my name is {}".format(kwargs['name'])
		if 'mother' in kwargs:
			print "my mother name is {}".format(kwargs['mother'])
		if 'location' in kwargs:
			print "my location is {}".format(kwargs['location'])
		if 'gender' in kwargs:
			print "my gender is {}".format(kwargs['gender'])

# 
print callme(name='kumar',mother='maa')
print callme(name='kumar',location='hyd')
print callme(name='kumar',location='hyd',gender='m')