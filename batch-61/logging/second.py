#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date or time.strftime().
import logging

logging.basicConfig(filename="log.txt",filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',datefmt='%c')

logging.debug("This is a debug message.")
logging.info("This is a info message.")
logging.warning("this is an warning message.")
logging.error("this is an error message.")
logging.critical("this is an critical message.")

'''
Logging :python first.py 
WARNING:root:this is an warning message.
ERROR:root:this is an error message.
CRITICAL:root:this is an critical message.
Logging :
'''