#!/usr/bin/python

class InvalidAgeException(Exception):
	def __init__(self,age):
		self.age = age

def validate_age(age):
	if age >= 18:
		return "Hey there welcome - you age {} is ok".format(age)
	else:
		raise InvalidAgeException(age)

age = int(raw_input("please enter the age:"))
try:
	validate_age(age)
except Exception as e:
	print "hey there you are still a kiddo - {}".format(e.age)
else:
	print validate_age(age)