#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# datefmt - man data ( linux command line)
# https://linux.die.net/man/1/date
import logging as l

l.basicConfig(filename='mylogs.txt',filemode='a',
		      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		      level=l.DEBUG,
		      datefmt='%c')

l.debug("This is an debug message")
l.info("This is an information message")
l.warning("This is an warning message")
l.error("This is an error message")
l.critical("This is an critical message")
