#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# time.strftime()
# man date

import logging as l

# basic config
l.basicConfig(filename="myapp.log",filemode='a',level=l.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# Loggers expose the interface that application code directly uses
# logger : root
# Handlers send the log records (created by loggers) to the appropriate destination.
# ex: filename="myapp.log",filemode='a'
# Filters provide a finer grained facility for determining which log records to output
# ex: level=l.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')


disk_size = int(raw_input("please enter the disk size:"))

if disk_size < 50:
	l.info("The disk is health at {}".format(disk_size))
elif disk_size < 70:
	l.warning("This disk seems to be filling up {}".format(disk_size))
elif disk_size < 85:
	l.error("The is disk is getting filled up {}".format(disk_size))
elif disk_size < 100:
	l.critical("The application has gone down  {}".format(disk_size))

