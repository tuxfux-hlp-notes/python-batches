#!/usr/bin/python
# Exception is a exception class.
# Exception is a parent/super class.
# 


class InvalidAge(Exception):
	def __init__(self,age):
		self.age = age


def validate_age(age):
	if age > 18:
		return "Welcome to the movie !!!"
	else:
		raise InvalidAge(age)


age = input("please enter your age:")

try:
	validate_age(age)
except Exception as e:
	print "Buddy!! you missed a chance to go over the movie - {}".format(18 - e.age)
else:
	print validate_age(age)

