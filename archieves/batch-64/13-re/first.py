#!/usr/bin/python

import re
answer = raw_input("will you come to the movies - yes/no ?")
if re.match(answer,'yes',re.I):
#if answer == 'yes' or answer == 'Yes':
	print "hey buddy welcome to the movie!!"
else:
	print "Better luck next time."