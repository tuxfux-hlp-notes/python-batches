#!/usr/bin/python
# default level - warning
# logging.basicConfig?
# logging.Formatter?
# man date
# time.strftime().

import logging as l
l.basicConfig(filename='mylog.txt',filemode='a',level=l.DEBUG,
			  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			  datefmt='%c')

# modes
# r -> read -> you can only read the file.
# a -> append -> you can only append the contents to the file.
# w -> write -> you can write to the file.
#   -> if you dont have a file a new file will be created.
#   -> if you have a file with data,the file gets truncated to zero.


l.debug("This is an debugging message.")
l.info("This is an info message.")
l.warning("This is an warning message.")
l.error("This is an error message.")
l.critical("This is an critical message.")

'''
* we can only log to FileHandler and StreamHandler.
* we cannot name our logger(root) to our choice.
* the default logger is root, for logging module.
'''