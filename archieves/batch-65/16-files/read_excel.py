#!/usr/bin/env python
from excel import OpenExcel
f = OpenExcel('names.xls')
print f.read('A')
print f.read('B')
name=f.read('A3')
gender=f.read('B3')
print "my name is {} and gender is {}".format(name,gender)