#!/usr/bin/python
# movie tickets


# sub class for Exception 
class InvalidAgeError(Exception):  # Exception is my parent class.
	def __init__(self,age):
		self.age = age

def validate_age(age):
	if age < 18:
		raise InvalidAgeError(age)
	else:
		return "Buddy!!! you are welcome to enjoy the movie!!!"


# Main
age = int(raw_input("please enter your age:"))

try:
	validate_age(age)
except Exception as e:
	print "Buddy!! you still need to grow up - {}".format(e.age)
else:
	print validate_age(age)


