#!/usr/bin/python
import re
with open('/var/log/syslog') as logfile:
	for log in logfile:
		m = re.search('k.*?n',log)
		print log[:m.start()] + log[m.end():]
