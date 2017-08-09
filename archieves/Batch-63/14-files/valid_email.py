#!/usr/bin/python
import re

reg = re.compile('[0-9a-z.]+@[a-z.]+',re.M)
f = open("my_emails.txt")
output = f.read()
print reg.findall(output)

