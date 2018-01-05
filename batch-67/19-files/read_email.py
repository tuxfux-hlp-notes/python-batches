#!/usr/bin/python
# TODO: my valid email address is tuxfux.hlp@gmail
import re
reg = re.compile('[a-z.0-9]+@[a-z.]+',re.I)

f = open('email.txt')
my_string = f.read()
f.close()

print reg.findall(my_string)
