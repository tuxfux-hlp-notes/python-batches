#!/usr/bin/python

'''
class Cup:
    def __init__(self):
        self.color = None      # public
        self.content = None    # public

    def fill(self, beverage):   # public
        self.content = beverage

    def empty(self):
        self.content = None


# public
Redcup = Cup()
print dir(Redcup)
Redcup.color = "Red"
Redcup.content = "tea"

print Redcup.color
print Redcup.content


# protected

class Cup:
    def __init__(self):
        self.color = None      # public
        self._content = None    # protected

    def fill(self, beverage):   # public
        self._content = beverage # protected

    def empty(self):
        self.content = None

# my expectations

Bluecup = Cup()
Bluecup._content="coffee"

print Bluecup._content

Bluecup.fill("chai")
print Bluecup._content

'''

# private
class Cup:
    def __init__(self):
        self.color = None      # public
        self.__content = None    # protected

    def fill(self, beverage):   # public
        self.__content = beverage # protected

    def empty(self):
        self.content = None

Whitecup = Cup()
print dir(Whitecup)
# ['_Cup__content', '__doc__', '__init__', '__module__', 'color', 'empty', 'fill']
"""
print Whitecup.__content
Traceback (most recent call last):
  File "chai.py", line 65, in <module>
    print Whitecup.__content
AttributeError: Cup instance has no attribute '__content'
"""
print Whitecup._Cup__content  # None
# Whitecup.__content = "white"
# print Whitecup.__content
