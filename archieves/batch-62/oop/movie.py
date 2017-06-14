#!/usr/bin/python
# inbuild - Exception - python exception - parent clas
# InvalidAgeException - Child class

class InvalidAgeException(Exception):
	def __init__(self,age):
		self.age = age

def validate_age(age):
	if age > 18:
		return "welcome to the movie!!!"
	else:
		raise InvalidAgeException(age)


if __name__ == '__main__':
		age = input("please enter your age:")

		try:
			validate_age(age)
		except InvalidAgeException as e:
			print "Buddy!! Go home and sleep you are still {}".format(e.age)
		else:
			print validate_age(age)