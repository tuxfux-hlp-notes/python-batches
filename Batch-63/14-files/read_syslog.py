#!/usr/bin/python

import re
reg = re.compile('[a-zA-Z]+-[a-zA-Z]+')

# reading the /var/log/syslog file line by line and removing the hostname name out of it
with open('/var/log/syslog') as f:
	for line in f:
		m = reg.search(line)
		print line[:m.start()] + line[m.end():]

'''
my_sentence='Jul 13 18:38:33 khyaathi-Technologies sublime_text[4380]: Source ID 4254038 was not found when attempting to remove it'

m = reg.search(my_sentence)
print m.start(),m.end()
print my_sentence[:m.start()] + my_sentence[m.end():]
'''