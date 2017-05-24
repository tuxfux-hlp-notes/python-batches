#!/usr/bin/python

import re
invite = raw_input("do you want to come to movie: ")

#if invite == 'yes':
if re.match(invite,'yes',re.I):
	print "sure!!! you are welcome to the movie!!"
else:
	print "hey!! better luck next time."