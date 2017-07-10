#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man data

import logging

logging.basicConfig(filename='my_logs.txt',filemode='a',level=logging.DEBUG,
	format='%(asctime)s - %(name)s  - %(levelname)s - %(message)s',datefmt='%c')

# Main
# to find out the information about my disk size.

disk_size = int(raw_input("please enter the disk size:"))

if disk_size < 50:
	logging.info("The disk looks health at {}".format(disk_size))
elif disk_size < 70:
	logging.warning("The disk is getting filled up {}".format(disk_size))
elif disk_size < 80:
	logging.error("your application is sleeping now {}".format(disk_size))

logging.debug("This is a debug message.")
logging.info("This is a info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is an critical message.")