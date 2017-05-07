#!/usr/bin/python
# logging.basicConfig? or help(logging.basicConfig)
# logging.Formatter?
# man date or www.google.com -> man date
# time.strftime()

import logging

logging.basicConfig(filename="my_disk.log",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
	datefmt='%c')

disk_size = int(raw_input("please enter the disk size:"))

if disk_size < 50:
	logging.info("The disk looks very healthy at {}.".format(disk_size))
elif disk_size < 70:
	logging.warning("The disk is getting filled up {}.".format(disk_size))
elif disk_size < 80:
	logging.error("The disk is puking errors {}.".format(disk_size))
elif disk_size < 99:
	logging.critical("your application is sleeping {}".format(disk_size))