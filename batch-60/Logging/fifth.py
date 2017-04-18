#!/usr/bin/python
# logging.basicConfig? or help(logging.basicConfig)
# logging.Formatter?
# man date or www.google.com -> man date
# time.strftime()

import logging
from subprocess import Popen,PIPE
import re

# create logger
logger = logging.getLogger('my_disk_app')  # logger
logger.setLevel(logging.DEBUG)               # filter for logger.

# create console handler and set level to debug
ch = logging.StreamHandler()                 # handler
ch.setLevel(logging.DEBUG)                   # filter for handler.

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter) # Handler and formatter

# add ch to logger
logger.addHandler(ch) # logger and handler.


#logging.basicConfig(filename="my_disk.log",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
#	datefmt='%c')

# Loggers expose the interface that application code directly uses.
# ex: Logger : root
# Handlers send the log records (created by loggers) to the appropriate destination.
# ex: Handler : filename="my_disk.log"
# Filters provide a finer grained facility for determining which log records to output.
# ex: Filter : level=logging.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',datefmt='%c' 

# disk_size = $(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g')
#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]
disk_size = int(re.search('([0-9]+)%',output).group(1))
#print disk_size


if disk_size < 50:
	logger.info("The disk looks very healthy at {}.".format(disk_size))
elif disk_size < 70:
	logger.warning("The disk is getting filled up {}.".format(disk_size))
elif disk_size < 80:
	logger.error("The disk is puking errors {}.".format(disk_size))
elif disk_size < 99:
	logger.critical("your application is sleeping {}".format(disk_size))


# basicConfig
# save into a file or a console.
# no logger defined.

