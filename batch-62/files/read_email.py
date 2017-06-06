#!/usr/bin/python
import re
reg = re.compile("[a-z0-9.]+@[a-z.]+")


f = open('my_emails.txt',"r")
my_emails = f.read()
f.close()

print reg.findall(my_emails)

