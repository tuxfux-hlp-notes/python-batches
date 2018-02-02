#!/usr/bin/python
'''
my_days = ['yesterday','today','tomorrow','dayafter']

a)
output:
yesterday 9
today     5
tomorrow  8
dayafter  8

In [24]: my_days = ['yesterday','today','tomorrow','dayafter']

In [25]: for day in my_days:
    ...:     print day,len(day)
    ...:     
yesterday 9
today 5
tomorrow 8
dayafter 8

In [26]: len(my_days)
Out[26]: 4

In [27]: len?
Docstring:
len(object) -> integer

Return the number of items of a sequence or collection.
Type:      builtin_function_or_method



b) 
output:
Yesterday
TOday
TOMorrow
DAYAafter

In [29]: my_days = ['yesterday','today','tomorrow','dayafter']

In [30]: for value in my_days:
    ...:     print value,my_days.index(value)
    ...:     
yesterday 0
today 1
tomorrow 2
dayafter 3

In [31]: for value in my_days:
    ...:     print value,my_days.index(value),value[my_days.index(value)]
    ...:     
    ...:     
yesterday 0 y
today 1 o
tomorrow 2 m
dayafter 3 a

In [32]: for value in my_days:
    ...:     print value,my_days.index(value),value[0:my_days.index(value)]
    ...:     
    ...:     
    ...:     
yesterday 0 
today 1 t
tomorrow 2 to
dayafter 3 day

In [33]: for value in my_days:
    ...:     print value,my_days.index(value),value[0:my_days.index(value) + 1]
    ...:     
    ...:     
    ...:     
    ...:     
yesterday 0 y
today 1 to
tomorrow 2 tom
dayafter 3 daya

In [34]: my_string="python"

In [35]: my_string[0:3]
Out[35]: 'pyt'

In [36]: my_string[:3]
Out[36]: 'pyt'

In [37]: my_string[3:]
Out[37]: 'hon'

In [38]: for value in my_days:
    ...:     print value[0:my_days.index(value) + 1].upper() + value[my_days.index(value) + 1:]
    ...:     
    ...:     
    ...:     
    ...:     
    ...:     
Yesterday
TOday
TOMorrow
DAYAfter


'''