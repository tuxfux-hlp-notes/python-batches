#!/usr/bin/python
# http://anandology.com/python-practice-book/object_oriented_programming.html#special-class-methods
# https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.pdf
# dunders
'''
In [1]: a = 1

In [2]: a.__
a.__abs__           a.__float__         a.__invert__        a.__pos__           a.__rlshift__       a.__setattr__
a.__add__           a.__floordiv__      a.__long__          a.__pow__           a.__rmod__          a.__sizeof__
a.__and__           a.__format__        a.__lshift__        a.__radd__          a.__rmul__          a.__str__
a.__class__         a.__getattribute__  a.__mod__           a.__rand__          a.__ror__           a.__sub__
a.__cmp__           a.__getnewargs__    a.__mul__           a.__rdiv__          a.__rpow__          a.__subclasshook__
a.__coerce__        a.__hash__          a.__neg__           a.__rdivmod__       a.__rrshift__       a.__truediv__
a.__delattr__       a.__hex__           a.__new__           a.__reduce__        a.__rshift__        a.__trunc__
a.__div__           a.__index__         a.__nonzero__       a.__reduce_ex__     a.__rsub__          a.__xor__
a.__divmod__        a.__init__          a.__oct__           a.__repr__          a.__rtruediv__      
a.__doc__           a.__int__           a.__or__            a.__rfloordiv__     a.__rxor__          

In [2]: b = 2

In [3]: a + b
Out[3]: 3

In [4]: a.__add__(b)
Out[4]: 3

In [5]: a = 
  File "<ipython-input-5-beb00c8a707f>", line 1
    a =
        ^
SyntaxError: invalid syntax


In [6]: c = "python"

In [7]: d = "rocks"

In [8]: c.__add__(d)
Out[8]: 'pythonrocks'

In [9]: # rational numbers

In [10]: # 1/2 + 1/3 = 5/6 

In [11]: 1/2 + 1/3
Out[11]: 0

In [12]: 1/2.0 + 1/3.0
Out[12]: 0.8333333333333333

'''


class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b a.__add__(b)
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
# case1:
a = RationalNumber(1, 2)
b = RationalNumber(1, 3)
print a + b

# case 2:
a = RationalNumber(1, 2)
b = 2 # 2/1
print a + b

# case 3:
a = 1
b = 1
print a + b

# case 4:
a = "python"
b = "rocks"
print a + b

