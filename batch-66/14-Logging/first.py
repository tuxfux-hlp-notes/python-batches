#!/usr/bin/python

import logging as l

l.debug("This is an debug message.")
l.info("This is an information message.")
l.warning("This is an warning message.")
l.error("This is an error message.")
l.critical("This is an critical message")

'''
The default level is WARNING, which means that only events of
this level and above will be tracked, unless the logging package is configured to do otherwise.

khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/batch-66/14-Logging$ python first.py 
WARNING:root:This is an warning message.
ERROR:root:This is an error message.
CRITICAL:root:This is an critical message
khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/batch-66/14-Logging$ 

DEBUG < INFO < WARNING < ERROR < CRITICAL



'''