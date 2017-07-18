#!/usr/bin/python
from excel import OpenExcel
f = OpenExcel('namesdb.xls')
print f.read('A2')
print f.read('B2')
print f.read('A')
print f.read('B')