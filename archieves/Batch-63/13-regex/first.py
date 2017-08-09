#!/usr/bin/python

import re

answer = raw_input("do you want to come to movie?")
#if answer == 'yes' or answer == 'Yes':
if re.match(answer,'yes',re.I):
	print "You are welcome to the movie."
else:
	print "Better luck next time."