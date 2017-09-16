#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter
# man date
# time.strftime()
# level -> debug < info < warning < error < critical
# crontab or scheduler
import logging
from subprocess import Popen,PIPE
import re

#logging.basicConfig(filename='mydisk.log',filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
#	datefmt='%c',level=logging.DEBUG)

# Advanced Logging
# * Loggers expose the interface that application code directly uses.
#  - ex: logger - root
#  - defines what should be name of your application.
#  - what logs should be logged in.
# * Handlers send the log records (created by loggers) to the appropriate destination.
#  - ex: filename='mydisk.log',filemode='a'
#  - https://docs.python.org/2/howto/logging.html#useful-handlers
# * Filters provide a finer grained facility for determining which log records to output.
#  - ex: level=logging.DEBUG
# * Formatters specify the layout of log records in the final output.
#  - ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s '

# Logging setup 


# create logger
logger = logging.getLogger('disk_monitor')   # logger name/Application name
logger.setLevel(logging.DEBUG)               # filter at logger level.

# create console handler and set level to debug
ch = logging.FileHandler(filename='mydisk.log')                 # handlers
ch.setLevel(logging.DEBUG)                   # filter at handler level.

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Formatter

# add formatter to ch
ch.setFormatter(formatter)  # handler to formatter

# add ch to logger
logger.addHandler(ch)   # logger to handler

# disk_info=$(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g')
p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','-1'],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]
disk_size = int(re.search('([0-9]+)%',output,re.M).group(1))

# main
if __name__ == '__main__':
	if disk_size < 50:
		logger.info("your disk looks health at {}".format(disk_size))
	elif disk_size < 70:
		logger.warning("Your disk is getting fat at {}".format(disk_size))
	elif disk_size < 80:
		logger.error("your disk is puking errors {}".format(disk_size))
	else:
		logger.critical("your application has gone for a sleep {}".format(disk_size))


