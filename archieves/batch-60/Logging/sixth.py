#!/usr/bin/python
# logging.basicConfig? or help(logging.basicConfig)
# logging.Formatter?
# man date or www.google.com -> man date
# time.strftime()
# https://docs.python.org/2/howto/logging.html#useful-handlers

import logging
from subprocess import Popen,PIPE
import re

# create logger
logger = logging.getLogger('my_disk_app')  # logger
logger.setLevel(logging.DEBUG)               # filter for logger.

# create console handler and set level to debug
ch = logging.FileHandler(filename="my_disk_app.log")                 # handler
ch.setLevel(logging.DEBUG)                   # filter for handler.

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter) # Handler and formatter

# add ch to logger
logger.addHandler(ch) # logger and handler.

# disk_size = $(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g')
#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
#p2.communicate()
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

