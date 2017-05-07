#!/usr/bin/python
# logging.basicConfig? or help(logging.basicConfig)
# logging.Formatter?
# man date or www.google.com -> man date
# time.strftime()

import logging

logging.basicConfig(filename="myapp.log",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
	datefmt='%c')

logging.debug("this is an debug information")
logging.info("this is an information message.")
logging.warning("this is an warning message.")
logging.error("this is an error message.")
logging.critical("this is an critcal message")