#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# time.strftime()
# man date

import logging
import re
from subprocess import Popen,PIPE



# create logger
logger = logging.getLogger('Disk_Monitor')  # logger
logger.setLevel(logging.DEBUG)				# filter for logger

# create console handler and set level to debug
# https://docs.python.org/2/howto/logging.html#useful-handlers
ch = logging.StreamHandler()  # Handler
ch.setLevel(logging.DEBUG)    # filter for handler level.

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)  # Handler and Formatter.

# add ch to logger
logger.addHandler(ch)       # logger and handler.


# Loggers expose the interface that application code directly uses
# logger : Disk_monitor
# Handlers send the log records (created by loggers) to the appropriate destination.
# ex: StreamHandler
# Filters provide a finer grained facility for determining which log records to output
# ex: filter for logger: logger.setLevel(logging.WARNING)
# ex: filter for handler: ch.setLevel(logging.DEBUG) 
# Formatters specify the layout of log records in the final output.
# ex: format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# disk_size=$(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##')
# disk_size = int(raw_input("please enter the disk size:"))

# shelx
# shelx("df -h /") => ['df','-h','/'] 
p = Popen(['df','-h','/'],stdout=PIPE)
p1 = Popen(['tail','-n','1'],stdout=PIPE,stdin=p.stdout)
output = p1.communicate()[0]
disk_size = int(re.search('([0-9]+)[%]',output).group(1))


if disk_size < 50:
	logger.info("The disk is health at {}".format(disk_size))
elif disk_size < 70:
	logger.warning("This disk seems to be filling up {}".format(disk_size))
elif disk_size < 85:
	logger.error("The is disk is getting filled up {}".format(disk_size))
elif disk_size < 100:
	logger.critical("The application has gone down  {}".format(disk_size))


