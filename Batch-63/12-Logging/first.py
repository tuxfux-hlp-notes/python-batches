#!/usr/bin/python
# The default level is WARNING, 
# which means that only events of this level and above will be tracked, 
# unless the logging package is configured to do otherwise.

import logging

logging.debug("This is a debug message.")
logging.info("This is a info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is an critical message.")

"""
khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/Batch-63/12-Logging$ python first.py 
WARNING:root:This is a warning message.
ERROR:root:This is an error message.
CRITICAL:root:This is an critical message.
khyaathi@khyaathi-Technologies:~/Documents/tuxfux-hlp-notes/python-notes/Batch-63/12-Logging$ 

"""
