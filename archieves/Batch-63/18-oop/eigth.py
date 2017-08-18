#!/usr/bin/python
# http://radek.io/2011/07/21/private-protected-and-public-in-python/

'''
# Public
class Cup:
    def __init__(self):
        self.color = None
        self.content = None
    def fill(self, beverage):
        self.content = beverage
    def empty(self):
        self.content = None
redcup = Cup()
print redcup.color
print redcup.content
redcup.color = "red"
redcup.content = "coffee"
print redcup.color
print redcup.content
# protected
class Cup:
    def __init__(self):
        self.color = None
        self._content = None
    def fill(self, beverage):
        self._content = beverage
    def empty(self):
        self._content = None
# main
bluecup = Cup()
print bluecup.color
print bluecup._content
bluecup.color = "blue"
bluecup._content = "coffee"
print bluecup.color
print bluecup._content
# my expectation .
bluecup.empty()
print bluecup._content
bluecup.fill("tea")
print bluecup._content
'''

# private
class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def show(self):
    	return self.__content

# Main
yellowcup = Cup(color="yellow")
print yellowcup._color
"""
#print yellowcup.__content
Traceback (most recent call last):
  File "08-program.py", line 71, in <module>
    print yellowcup.__content
AttributeError: Cup instance has no attribute '__content'
"""
yellowcup.empty()
print yellowcup.show()
yellowcup.fill(beverage="boost")
print yellowcup.show()

## name mangling

print yellowcup._Cup__content
