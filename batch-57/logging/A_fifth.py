#!/usr/bin/python
 
# Loggers expose the interface that application code directly uses.
# Handlers send the log records (created by loggers) to the appropriate destination.
# Filters provide a finer grained facility for determining which log records to output.
# Formatters specify the layout of log records in the final output.

# crontab or scheduler.
 
import logging as l
from subprocess import Popen,PIPE
import re

#l.basicConfig(filename="disk_log.txt",filemode="a",level=l.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')
# logger - root
# Handlers - ex: filename="disk_log.txt",filemode="a",
# Filters - ex: level=l.DEBUG
# Formatter - ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c'


# create logger
logger = logging.getLogger('Disk Monitor')   # logger
logger.setLevel(logging.DEBUG)               # Filter for logger.

# create console handler and set level to debug
ch = logging.StreamHandler()                 # handler
ch.setLevel(logging.DEBUG)                   # Filter for handler.

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   # formatter

# add formatter to ch
ch.setFormatter(formatter)  #  handler and formatter

# add ch to logger
logger.addHandler(ch)       #  logger and handler


# Main program
if __name__ == '__main__':
	#disk_size = int(raw_input("please enter the disk size to check ?"))
	p1 = Popen(["df","-h","/"],stdout=PIPE)
	p2 = Popen(["tail","-n","1"],stdin=p1.stdout,stdout=PIPE)
	output = p2.communicate()[0]
	disk_size = int(re.search('([0-9]+)%',output).group(1))

	if disk_size < 50:
		logger.info("The disk looks health at {}".format(disk_size))
	elif disk_size < 70:
		logger.warning("The disk is puking some warning at {}".format(disk_size))
	elif disk_size < 90:
		logger.error("The disk seems to have some errors at {}".format(disk_size))
	elif disk_size < 100:
		logger.critical("you disk is having some errors at {}".format(disk_size))
