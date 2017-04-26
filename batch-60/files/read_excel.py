#!/usr/bin/python
# https://github.com/tuxfux-hlp/Python-examples/blob/master/files/my_read.py

from excel import OpenExcel
f = OpenExcel('names.xls')
print f.read('A')
print f.read('B')
print "{} is a {}".format(f.read('A8'),f.read('B8'))