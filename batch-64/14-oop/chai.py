#!/usr/bin/python
# radek.io/2011/07/21/private-protected-and-public-in-python/

# private
class Cup:
    def __init__(self):
        self._color = None # private variable
        self.__content = None # protected variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def whatincup(self):
    	return self.__content

pinkcup = Cup()
pinkcup._color="pink"

pinkcup.fill("boost")
print pinkcup.whatincup()

# name mangling
pinkcup._Cup__content = "horlicks" 
print pinkcup._Cup__content
print pinkcup.__content


'''
# protected

class Cup:
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

yellowcup = Cup()
yellowcup.color="yellow"
yellowcup._content="cofee"
print yellowcup.color
print yellowcup._content

# public
class Cup:
    def __init__(self):
        self.color = None  # public
        self.content = None # public

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

Redcup = Cup()
Redcup.color="red"
#Redcup.fill("chai")
Redcup.content="chai"
print Redcup.color
print Redcup.content
'''