#!/usr/bin/python

import logging as l

l.debug("This is an debug message")
l.info("this is an informational message")
l.warning("this is an warning message")
l.error("This is an error message")
l.critical("This is an critical message")


'''
output:
WARNING:root:this is an warning message
ERROR:root:This is an error message
CRITICAL:root:This is an critical message

explanation:
The default level is WARNING, which means that only events of this level and above will be tracked, 
unless the logging package is configured to do otherwise.
'''