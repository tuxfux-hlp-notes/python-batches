#!/usr/bin/python
#http://anandology.com/python-practice-book/object_oriented_programming.html#special-class-methods
# Magic Methods
#http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods
#http://farmdev.com/src/secrets/magicmethod/


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
        return RationalNumber(n, d)

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__

# Main
a = RationalNumber(1, 2)
b = RationalNumber(1, 3)
print a + b  # a.__add__(b)

e = RationalNumber(1,2) # instance of the RationalNumber clas.
f = 3 # instance of the Integer class.
# f = RationalNumber(f)
# f = RationalNumber(3,1)
print e + f  # e.__add__(f)

c = 1  # c is an instance of integer class
d = 2  # di is an instance of integer class
print c + d
