#!/usr/bin/python
# xlrd example - https://github.com/tuxfux-hlp/Python-examples/blob/master/files/my_read.py
from excel import OpenExcel
f = OpenExcel('names_db.xls')
print f.read('A')
print f.read('B') 
print "{} is a {}".format(f.read('A4'),f.read('B4'))