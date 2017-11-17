#!/usr/bin/python

import re

answer = raw_input("will you come to a movie?")
#if answer == 'yes' or answer == 'Yes':
if re.match(answer,'yes',re.I):
	print "you are welcome to the movie"
else:
	print "Better luck next time"