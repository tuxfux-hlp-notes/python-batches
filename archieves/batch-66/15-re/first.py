#!/usr/bin/python
import re
answer = raw_input("do you want to come to movie: yes/no - ")
#if answer == 'yes':
if re.match(answer,'yes',re.I):
	print "Cool buddy!!! come by 7pm."
else:
	print "Thats ok !!! Better luck next time."