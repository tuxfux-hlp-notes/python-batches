#!/usr/bin/env python
from excel import OpenExcel
f = OpenExcel('namesdb.xls')
print f.read('A') # read 'A' row
print f.read('B')
print "{} is gender {}".format(f.read('A2'),f.read('B2'))