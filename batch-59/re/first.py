#!/usr/bin/python

import re
answer = raw_input("do you want to come to the movies ? yes/no: ")

#if answer == 'yes':
if re.match(answer,'yes',re.I):
	print "hey!! welcome to the movie!!"
else:
	print "your wish !! Better luck next time."