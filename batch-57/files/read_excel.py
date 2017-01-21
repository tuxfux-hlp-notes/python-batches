#!/usr/bin/python
from excel import OpenExcel
f = OpenExcel('names.xls')
print f.read('A')
print "my name is {} and my gender is {}".format(f.read('A3'),f.read('B3'))
