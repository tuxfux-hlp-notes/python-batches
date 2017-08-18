#!/usr/bin/python

# InvalidAgeException - child class
# Exception - Parent class

class InvalidAgeException(Exception):
	def __init__(self,age):
		self.age = age

def validate_age(age):
	if age < 18:
		raise InvalidAgeException(age)
	else:
		return "Welcome to the theater. You are eligible to see the movie." 

# Main
age = int(raw_input("please enter the age:"))

try:
	validate_age(age)
except InvalidAgeException as e:
	print "Buddy!! you are still young to see the movies - {}".format(e.age)
else:
print validate_age(age)
