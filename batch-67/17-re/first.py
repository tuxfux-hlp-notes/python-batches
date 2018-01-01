#!/usr/bin/python
import re

answer = raw_input("do you want to come to movie - yes/no:")

if re.match(answer,'yes',re.I):
#if answer == 'yes':
	print "welcome to the movie!!!"
else:
	print "Better luck next time!!!"