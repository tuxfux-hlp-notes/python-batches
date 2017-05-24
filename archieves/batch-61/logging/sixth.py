#!/usr/bin/python
# cron - linux
# scheduler - window
# logging.Formatter?
# SyslogHandler

import logging
from logging.handlers import SysLogHandler
from subprocess import Popen,PIPE

# create logger
logger = logging.getLogger('Disk Monitor')  # logger defination with name.
logger.setLevel(logging.DEBUG)                # filter for the logger.

# create console handler and set level to debug
# syslogs
# /var/log/syslog - ubuntu/linuxmint
# /var/log/messages - redhat

Fh = SysLogHandler(address="/dev/log")                  # handler
Fh.setLevel(logging.DEBUG)                    # filter for handlers

# create formatter
formatter = logging.Formatter(' %(name)s : %(levelname)s - %(message)s')

# add formatter to ch
Fh.setFormatter(formatter)  # handler and formatter.

# add ch to logger
logger.addHandler(Fh)       # logger and handler.


#logging.basicConfig(filename="disk.log",filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',datefmt='%c')

# Loggers expose the interface that application code directly uses.
# ex: logger : root
# Handlers send the log records (created by loggers) to the appropriate destination.
# reference: https://docs.python.org/2/howto/logging.html#useful-handlers
# ex: filename="disk.log",filemode='a'
# Filters provide a finer grained facility for determining which log records to output
# ex: level=logging.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',datefmt='%c'

# main
if __name__ == '__main__':
	
	# disk_size = $(df -h / | tail -n 1 | awk '{print $5}'|sed -e 's#%##g')
	#disk_size = int(raw_input("please enter the disk size:"))

	p1 = Popen(['df','-h','/'],stdout=PIPE)
	p2 = Popen(['tail','-n','-1'],stdin=p1.stdout,stdout=PIPE)
	output = p2.communicate()[0]
	disk_size = int(output.split()[4].split('%')[0])

	if disk_size < 50:
		logger.info("Your disk looks health at {}.".format(disk_size))
	elif disk_size < 70:
		logger.warning("your disk is getting filled up {}.".format(disk_size))
	elif disk_size < 80:
		logger.error("Your disk is puking errors at {}.".format(disk_size))
	else:
		logger.critical("your disk is dead. Please clean the logs - {}.".format(disk_size))


# challenges
# * logger name - root
# redirect to a file. (ex: syslog handler,email)
