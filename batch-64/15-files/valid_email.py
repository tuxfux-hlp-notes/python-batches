#!/usr/bin/python

import re
reg = re.compile('[0-9a-z.]+@[a-z.]+')

f = open("valid_email.txt")
email_data = f.read()
f.close()

#print email_data

print reg.findall(email_data)