#!/usr/bin/python
from excel import OpenExcel
f = OpenExcel('namesdb.xls')
print f.read('A')
print f.read('B')
print f.read('A4')