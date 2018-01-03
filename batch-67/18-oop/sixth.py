#!/usr/bin/python

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

 # main
a = RationalNumber(1, 2)
b = RationalNumber(1, 3)
print a + b  # a.__add__(self,b)

a = RationalNumber(1, 2) # 1/2
b = 12 # b = RationalNumber(12,1) , 12/1
print a + b

a = 10
b = 20
print a + b # 30