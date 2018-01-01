#!/usr/bin/python
import re

my_friends = ['sridhar','ravi','balu','rajesh','kumar','phani']
for value in my_friends:
	if re.match('^.....$',value):
		print re.match('^.....$',value).group()