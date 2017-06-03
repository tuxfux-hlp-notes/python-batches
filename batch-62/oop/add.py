#!/usr/bin/python
# magic methods or dunders
# references
# https://github.com/RafeKettler/magicmethods
# http://anandology.com/python-practice-book/object_oriented_programming.html#special-class-methods
# 1/2 + 1/3 = 5/6
'''
In [7]: a = 1

In [8]: print type(a)
<type 'int'>

In [9]: print dir(a)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']

In [10]: # a is a object of integer class

In [11]: # __add__ : ex: of a dunder or magic method

In [12]: b = 1

In [13]: a + b
Out[13]: 2

In [14]: a.__add__(b)
Out[14]: 2

In [15]: c="linux"

In [16]: d=" rocks"

In [17]: c.__add__(d)
Out[17]: 'linux rocks'
'''

class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)  # a.n = 1,a.d = 2
        >>> b = RationalNumber(1, 3)  # b.n = 1,b.d = 3
        >>> a + b  a.__add__(b) or a.__add__(other)
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


# case1
a = 1  # object of int class
b = 1  # object of int class
print a + b  # 2

# case 2
a = RationalNumber(2,3)
b = RationalNumber(2,5)
print a + b  # 16/15

# case 3
a = RationalNumber(2,3)
b = 2  # 2/1
print a + b # 8/3