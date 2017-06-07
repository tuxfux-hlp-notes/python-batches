#!/usr/bin/python
# reading from excel using the excel module.
# xlrd.
from excel import OpenExcel
f = OpenExcel('names_db.xls')
print f.read('A')
print f.read('B')
print "my name is {} and my gender is {}".format(f.read('A6'),f.read('B6'))