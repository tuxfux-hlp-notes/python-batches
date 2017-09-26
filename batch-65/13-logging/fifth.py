#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# shelx
# crontab or scheduler
# https://docs.python.org/2/library/subprocess.html
import logging
from subprocess import Popen,PIPE

# if __name__ == '__main__':
# 		l.basicConfig(filename='disklog.txt',filemode='a',
# 				      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# 				      level=l.DEBUG,
# 				      datefmt='%c')

# logger - expose the interface that application code directly uses
# logger - root
# Handler - send the log records (created by loggers) to the appropriate destination.
# ex: https://docs.python.org/2/howto/logging.html#useful-handlers
# ex: filename='disklog.txt',filemode='a'
# Filter - provide a finer grained facility for determining which log records to output.
# ex: level=l.DEBUG
# Formatter - specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c'

# create logger
logger = logging.getLogger('Disk Monitor') # logger
logger.setLevel(logging.DEBUG)				 # filter for logger

# create console handler and set level to debug
ch = logging.FileHandler('disklog.txt')                 # handler
ch.setLevel(logging.DEBUG)                   # filter for handlers

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter) # handler and formatter

# add ch to logger
logger.addHandler(ch)     # logger and handler

if __name__ == '__main__':
# disk_value = $(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g')
		#disk_value = int(raw_input("Please enter the disk size:"))
		p1 = Popen(['df','-h','/'],stdout=PIPE)
		p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
		disk_value = int(p2.communicate()[0].split()[-2].split('%')[0])

	
		if disk_value < 50:
			logger.info("The disk looks healthy {}".format(disk_value))
		elif disk_value < 70:
			logger.warning("Your disk is gettting fat {}".format(disk_value))
		elif disk_value < 80:
			logger.error("Your disk is puking {}".format(disk_value))
		else:
			logger.critical("your application has gone into coma - {}".format(disk_value))

'''
* logger name - multiple logs in same file create confusion.
* handlers - you can put logs only to files.
* we cannot push it to a larger audience.
'''