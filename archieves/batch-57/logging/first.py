#!/usr/bin/python
import logging as l

l.debug("this is an debugging message")
l.info("this is an informational message")
l.warning("this is a warning message")
l.error("This is an error message")
l.critical("This is an critical message")

logging.FileHandler('all_logs.txt')  