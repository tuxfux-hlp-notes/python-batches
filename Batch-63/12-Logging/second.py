#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man data

import logging

logging.basicConfig(filename='my_logs.txt',filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s  - %(levelname)s - %(message)s',datefmt='%c')

logging.debug("This is a debug message.")
logging.info("This is a info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is an critical message.")