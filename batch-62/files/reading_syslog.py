#!/usr/bin/python
# reading out a huge file.
'''
In [1]: my_string='Jun  6 19:10:27 khyaathi-Technologies sublime_text[2679]: Source ID 613295 was not found when attempting to remove it'

In [2]: reg = re.compile('\w+-\w+',re.I)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-a00dc91693f8> in <module>()
----> 1 reg = re.compile('\w+-\w+',re.I)

NameError: name 're' is not defined

In [3]: import re

In [4]: reg = re.compile('\w+-\w+',re.I)

In [5]: m = reg.search(my_string)

In [6]: m.
m.end        m.expand     m.groupdict  m.lastgroup  m.pos        m.regs       m.start      
m.endpos     m.group      m.groups     m.lastindex  m.re         m.span       m.string     

In [6]: m.start()
Out[6]: 16

In [7]: m.end()
Out[7]: 37

In [8]: print my_string[:m.start()] + my_string[m.end():]
Jun  6 19:10:27  sublime_text[2679]: Source ID 613295 was not found when attempting to remove it

'''

import re
reg = re.compile('\w+-\w+',(re.I|re.M))

with open("/var/log/syslog","rb") as f:
	for line in f:
		m = reg.search(line)
		print line[:m.start()] + line[m.end():]

