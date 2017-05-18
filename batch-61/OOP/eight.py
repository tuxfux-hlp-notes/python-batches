#!/usr/bin/python
# example of rational numbers
# polymorphism
# dunters - https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.pdf

'''
1/2 + 1/3 = 1*3 + 2 * 1/(2*3) = 5/6
'''

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


# Main program
# string,numbers and rational numbers
a = RationalNumber(1, 2)  # a.n = 1 , a.d = 2
b = RationalNumber(1, 3)  # b.n = 1 , b.d = 3
print a + b  # a.__add__(b) , return RationalNumber(5,6) __add__ is a method from RationalNumber class.

x = RationalNumber(1, 2)  # instance of RationalNumber class
y = 5                     # instance of the int class
print x + y # x.__add__(y) y = RationalNumber(5,1) # 5/1

c = 10 # int
d = 20 # int
print c + d # c.__add__(d)  # __add__ is a method from int class.

e = "python" # str
f = " rocks"  # str
print e + f  # e.__add__(f) # __add__ is a method from str class.














'''
In [1]: a = 1

In [2]: b = 2

In [3]: a + b
Out[3]: 3

In [4]: print dir(a)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']

In [5]: # dunders or magic methods

In [6]: # integers,floats,strings - objects

In [7]: # a is a object/instance of the class int

In [8]: type(a)
Out[8]: int

In [9]: print type(a)
<type 'int'>

In [10]: print type(b)
<type 'int'>


In [12]: print a.__add__(b)
3

In [13]: c = "python"

In [14]: d = " rocks"

In [15]: print c.__add__(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-8294982a7480> in <module>()
----> 1 print c.__add__(b)

TypeError: cannot concatenate 'str' and 'int' objects

In [16]: print c.__add__(d)
python rocks


'''