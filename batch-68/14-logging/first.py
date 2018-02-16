#!/usr/bin/python

'''
The default level is WARNING, which means that only events of this level and
 above will be tracked, unless the logging package is configured to do otherwise.

root@khyaathipython:~/Documents/git_repos/python-batches/batch-68/14-logging# python first.py 
WARNING:root:This is an warning message.
ERROR:root:This is an error message.
CRITICAL:root:This is an critical message.
root@khyaathipython:~/Documents/git_repos/python-batches/batch-68/14-logging# 


'''

import logging as l

l.debug("This is an debugging message.")
l.info("This is an info message.")
l.warning("This is an warning message.")
l.error("This is an error message.")
l.critical("This is an critical message.")