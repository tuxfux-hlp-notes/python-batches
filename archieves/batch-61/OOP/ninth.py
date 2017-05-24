#!/usr/bin/python
# encapsulation
# public,protected and private
# radek.io/2011/07/21/private-protected-and-public-in-python/
# https://importantshock.wordpress.com/2006/11/03/adventures-in-pythonic-encapsulation/
# https://github.com/tuxfux-hlp/Python-examples/blob/master/opps/Good_links.txt

'''
# public
class Cup:
    def __init__(self):
        self.color = None  # public
        self.content = None # public

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None


# main

Redcup = Cup()
print Redcup.color
print Redcup.content
Redcup.fill("tea")
print Redcup.content
Redcup.empty()
print Redcup.content

Redcup.content = "tea"
print Redcup.content


# protected
class Cup:
    def __init__(self):
        self.color = None  # public
        self._content = None # protected.

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None

# main

Redcup = Cup()
Redcup.fill("coffee")
print Redcup._content
Redcup.empty()
print Redcup._content
Redcup._content = "bru"
print Redcup._content

'''

# private

class Cup:
    def __init__(self):
        self._color = None  # protected
        self.__content = None # private

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

    def whatsthere(self):
    	return self.__content

# main

Redcup = Cup()
Redcup.fill("coffee")
print Redcup.whatsthere()
Redcup.empty()
print Redcup.whatsthere()
#print Redcup.__content
"""
Traceback (most recent call last):
  File "ninth.py", line 82, in <module>
    print Redcup.__content
AttributeError: Cup instance has no attribute '__content'
"""
Redcup._Cup__content = "tata"
print Redcup._Cup__content

