#!/usr/bin/python
import logging as l
l.debug("This is an debug message")
l.info("This is an information message")
l.warning("This is an warning message")
l.error("This is an error message")
l.critical("This is an critical message")

'''
The default level is WARNING, which means that only events of this 
level and above will be tracked, unless the logging package is configured to do otherwise.
'''