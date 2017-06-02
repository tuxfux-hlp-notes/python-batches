#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date or  time.strftime()
# scheduler - cron or scheduler - crontab

import logging
from subprocess import Popen,PIPE
from logging.handlers import SysLogHandler

#logging.basicConfig(filename="diskapp.log",filemode='a',level=logging.DEBUG,
#	format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s',
#	datefmt = '%c')

# Loggers expose the interface that application code directly uses.
# ex: logger - root
# Handlers send the log records (created by loggers) to the appropriate destination
# ex: filename="diskapp.log",filemode='a'
# Filters provide a finer grained facility for determining which log records to output.
# level=logging.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt = '%c'


# create logger
logger = logging.getLogger('Disk monitor') # logger
logger.setLevel(logging.DEBUG)             # filter at a logger level.

# create console handler and set level to debug
# https://docs.python.org/2/howto/logging.html#useful-handlers
ch = SysLogHandler(address="/dev/log")               # handler
ch.setLevel(logging.DEBUG)                 # filter at a handler level.

# create formatter
formatter = logging.Formatter(':  %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter) # handler and formatter

# add ch to logger
logger.addHandler(ch)      # logger and handler

# Main
# disk_size=$(df -h / | tail -n 1|awk '{print $5}'|sed -e 's#%##g')
#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','-1'],stdin=p1.stdout,stdout=PIPE)
output=p2.communicate()[0]
disk_size = int(output.split()[4].split('%')[0])


if __name__ == '__main__':
	if disk_size < 50:
		logger.info("The disk looks healthy at {}.".format(disk_size))
	elif disk_size < 70:
		logger.warning("Looks the disk is getting filledup at {}".format(disk_size))
	elif disk_size < 80:
		logger.error("Looks the disk is puking errors at {}".format(disk_size))
	elif disk_size < 99:
		logger.critical("My application is sleeping at {}".format(disk_size))

# basicConfig
# we can only log to a file or a console.
# in a single file - we want to rediret logs from multiple apps. - its going to be hard.
