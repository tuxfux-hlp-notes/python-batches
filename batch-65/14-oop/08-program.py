#!/usr/bin/python

class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
  		a + b => a.__add__(b)

  		In [42]: isinstance?
		Docstring:
		isinstance(object, class-or-type-or-tuple) -> bool

		Return whether an object is an instance of a class or of a subclass thereof.
		With a type as second argument, return whether that is the object's type.
		The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
		isinstance(x, A) or isinstance(x, B) or ... (etc.).
		Type:      builtin_function_or_method

		In [43]: isinstance(a,int)
		Out[43]: True

		In [44]: isinstance(a,str)
		Out[44]: False

		In [45]: isinstance(my_string,str)
		Out[45]: True



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
print a + b

a = RationalNumber(1, 2) # 1/2
b = 0 # b = RationalNumber(b) -> 0/1
print a + b

a = 1
b = 2
print a + b

a = "python"
b = "rocks"
print a + b