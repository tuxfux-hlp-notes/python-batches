#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# time.strftime()
# man date

import logging as l

# basic config
l.basicConfig(filename="myapp.log",filemode='a',level=l.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

l.debug("This is an debug message")
l.info("This is an info message")
l.warning("This is an warning message")
l.error("This is an error message")
l.critical("This is an critical message")

