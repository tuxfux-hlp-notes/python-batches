#!/usr/bin/python
# bigcinemas


class InvalidAge(Exception):
	def __init__(self,age):
		self.age = age

def validate_age(age):
	if age < 18:
		raise InvalidAge(age)
	else:
		return "Welcome to the movies!!"


age = int(raw_input("please enter your age:"))
#print validate_age(age)


try:
	validate_age(age)
# except Exception as e:
except InvalidAge as e:
	print "Buddy!!  you are very young at {}!! Grow up a bit.".format(e.age)
else:
	print validate_age(age)
