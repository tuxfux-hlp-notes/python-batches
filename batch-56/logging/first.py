#!/usr/bin/python
# logging.basicConfig
# Messages on screen or file like object - StreamHandlers
# logging.Formatter
# man date/https://docs.python.org/2/library/time.html#time.strftime
# 

import logging
logging.basicConfig(filename="myapp.log",filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# modes
# r - read mode - reading a file.
# w - write mode - write to a file. if file doesnot exist it should create it.
# if it exist truncates it to zero.
# a - append mode - appends contents to the file.

logging.debug("this is a debug message")
logging.info("this is an info message")
logging.warning("this is an warning message")
logging.error("this is an error message")
logging.critical("this is an critical message")
