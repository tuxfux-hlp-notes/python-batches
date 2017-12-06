#!/usr/bin/python
# movie related exception - InvalidAgeException
# Exception is our parent class

class InvalidAgeException(Exception):
	def __init__(self,age):
		self.age = age

def validate_age(age):
	if age < 18:
		raise InvalidAgeException(age)
	else:
		return "Welcome to the movie !!!"

## main

if __name__ == '__main__':
	age = int(raw_input("please enter your age: > 18 - "))
	try:
		validate_age(age)
	except Exception as e:
		print "sorry!!! you are still a kiddo {}".format(e.age)
	else:
		print validate_age(age)


