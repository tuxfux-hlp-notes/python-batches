#!/usr/bin/python
# http://anandology.com/python-practice-book/object_oriented_programming.html#special-class-methods
# https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.markdown

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
        return RationalNumber(n, d) # __str__

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__

# Main
# example 1
a = RationalNumber(1, 2) # 1/2
b = RationalNumber(1, 3) # 1/3
print a + b # a.__add__(b)

# example 2
a = RationalNumber(1, 2) # a is a instance of RationalNumber class
b = 10 # b is a instance of int class
# b = RationalNumber(10) => RationalNumber(10,1)
print a + b # 1/2 + 10/1 = (1*1 + 2 * 10)/2*1 = 21/2

# example 3
a = 10  # a is a instance of int class
b = 20  # b is a instance of int class
print a + b





'''
In [1]: a = 1
In [2]: b = 2
In [3]: type(a)
Out[3]: int
In [4]: type(b)
Out[4]: int
In [5]: # a,b are instance of class int
In [6]: a.
a.bit_length   a.conjugate    a.denominator  a.imag         a.numerator    a.real         
In [6]: a.__
a.__abs__           a.__doc__           a.__init__          a.__nonzero__       a.__reduce__        a.__rrshift__       a.__subclasshook__
a.__add__           a.__float__         a.__int__           a.__oct__           a.__reduce_ex__     a.__rshift__        a.__truediv__
a.__and__           a.__floordiv__      a.__invert__        a.__or__            a.__repr__          a.__rsub__          a.__trunc__
a.__class__         a.__format__        a.__long__          a.__pos__           a.__rfloordiv__     a.__rtruediv__      a.__xor__
a.__cmp__           a.__getattribute__  a.__lshift__        a.__pow__           a.__rlshift__       a.__rxor__          
a.__coerce__        a.__getnewargs__    a.__mod__           a.__radd__          a.__rmod__          a.__setattr__       
a.__delattr__       a.__hash__          a.__mul__           a.__rand__          a.__rmul__          a.__sizeof__        
a.__div__           a.__hex__           a.__neg__           a.__rdiv__          a.__ror__           a.__str__           
a.__divmod__        a.__index__         a.__new__           a.__rdivmod__       a.__rpow__          a.__sub__           
In [6]: a + b
Out[6]: 3
In [7]: a.__add__(b)
Out[7]: 3
In [8]: a = "linux"
In [9]: b = " rocks"
In [10]: a.__add__(b)
Out[10]: 'linux rocks'
In [11]: c = 1
In [12]: a
Out[12]: 'linux'
In [13]: c
Out[13]: 1
In [14]: a + c
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-ca57d551b7f3> in <module>()
----> 1 a + c
TypeError: cannot concatenate 'str' and 'int' objects
'''
