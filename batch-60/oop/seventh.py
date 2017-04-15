#!/usr/bin/python
# https://archive.org/details/magicmethods
# https://github.com/RafeKettler/magicmethods
# https://github.com/tuxfux-hlp/Python-examples/blob/master/opps/Good_links.txt
# http://anandology.com/python-practice-book/object_oriented_programming.html#special-class-methods

class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)  # __str__

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__


# basics
a = 1
b = 1
print a,type(a)
print b,type(b)
print a + b

# using RationalNumber
c = RationalNumber(1,4)
d = RationalNumber(1,5)
print c + d # c.__add__(other)

# using RationalNumber
e = RationalNumber(1,4)
f = 2
print e + f
