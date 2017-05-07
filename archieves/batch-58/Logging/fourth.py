#!/usr/bin/python
# Advanced example of logging.
# StreamHandler.

import logging
from subprocess import Popen,PIPE
import re


# create logger
logger = logging.getLogger('disk_logs')    # logger name.
logger.setLevel(logging.DEBUG)                  # filter for logger.

# create console handler and set level to debug
# https://docs.python.org/2/howto/logging.html#useful-handlers
ch = logging.StreamHandler()                    # handler
ch.setLevel(logging.DEBUG)                      # filter for handler.

# create formatter
# logging.Formatter?
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)  # set formatter to my handler ch.

# add ch to logger
logger.addHandler(ch)  # set logger to my handler


p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]
disk_size = int(re.search('([0-9]+)%',output).group(1))

if disk_size < 60:
	logger.info("The disk is healthy at {}.".format(disk_size))
elif disk_size < 75:
	logger.warning("The disk is getting filled up {}".format(disk_size))
elif disk_size < 85:
	logger.error("We are not able to write huge chunks at {}".format(disk_size))
elif disk_size < 100:
	logger.critical("The disk is completly filled up at {}".format(disk_size))
