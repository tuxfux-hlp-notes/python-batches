#!/usr/bin/python
# l.basicConfig?
# l.Formatter?
# man date or time.strftime()
# subprocess:https://docs.python.org/2/library/subprocess.html
# crontab or scheduler
# shelx
# handlers: https://docs.python.org/2/howto/logging.html#useful-handlers
# lh.SysLogHandler?

import logging
from logging.handlers import SysLogHandler
from subprocess import Popen,PIPE



# l.basicConfig(filename='myapp.log',filemode='a',level=l.DEBUG,
# 			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# 			datefmt='%c')


# create logger
logger = logging.getLogger('disk_monitor')  # logger name
logger.setLevel(logging.DEBUG)	            # filter for logger name.

# create console handler and set level to debug
ch = SysLogHandler(address="/dev/log")                # handler
ch.setLevel(logging.DEBUG)                  # filter for handler.

# create formatter
formatter = logging.Formatter('- %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)  # handler and formatter

# add ch to logger
logger.addHandler(ch)       # logger and handler


# Loggers expose the interface that application code directly uses.
# ex: root
# Handlers send the log records (created by loggers) to the appropriate destination.
# ex: filename='myapp.log',filemode='a'
# Filters provide a finer grained facility for determining which log records to output.
# ex: level=l.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c'

if __name__ == '__main__':
	#disk_size = int(raw_input("please enter the disk size:"))
	p1 = Popen(['df','-h','/'],stdout=PIPE)
	p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
	disk_size = int(p2.communicate()[0].split()[-2].split('%')[0])
	
	if disk_size < 50:
		logger.info("Your disk looks healthy at {}.".format(disk_size))
	elif disk_size < 70:
		logger.warning("seems our disk is incresing {}.Make sure you keep a track".format(disk_size))
	elif disk_size < 80:
		logger.error("our application is about to choke at {}.".format(disk_size))
	elif disk_size < 99:
		logger.critical("our application is down - {}".format(disk_size))