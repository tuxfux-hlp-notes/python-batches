#!/usr/bin/python

class InvalidAgeException(Exception):
	def __init__(self,age):
		self.age = age

# main
def validate_age(age):
	if age > 18:
		return "buddy!!! Enjoy the movie."
	else:
		raise InvalidAgeException(age)


age = int(raw_input("please enter your age:"))

try:
	validate_age(age)
except InvalidAgeException as e:
	print "you are yet to grow bud {}".format(e.age)
else:
	print validate_age(age)
