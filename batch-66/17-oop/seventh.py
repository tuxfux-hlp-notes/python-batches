#!/usr/bin/python
# https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.pdf
# magic methods or dunders.
class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b  a.__add__(b)
        5/6
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

 ## main
a = RationalNumber(1,2)  # a.n=1,a.d=2
b = RationalNumber(1,3)  # b.n=1,b.d=3
#print a + b  # a.__add__(b)
# n = self.n(1) * other.d(3) + self.d(2) * other.n(1) = 5
# d = self.d(2) * other.d(3) = 6
# return RationalNumber(n(5),d(6)) => self.n =5,self.d=6
# 5/6
print a + b

a = RationalNumber(1,2) # instance of RationalNumber class.
b = 10                  # instance of integer class.
# b = RationalNumber(10,1) # 10/1
print a + b  # 1/2 + 10/1 = 1 + 20/2 = 21/2

a = 1
b = 2
print a + b # 3