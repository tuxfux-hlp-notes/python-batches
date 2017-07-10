#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man data or time.strftime().
# https://docs.python.org/2/library/subprocess.html
# cronjob or scheduler
# import logging.handlers for rest all handlers.

from subprocess import Popen,PIPE

import logging

#logging.basicConfig(filename='my_logs.txt',filemode='a',level=logging.DEBUG,
#	format='%(asctime)s - %(name)s  - %(levelname)s - %(message)s',datefmt='%c')

# Loggers expose the interface that application code directly uses.
# ex:logger - root
# Handlers send the log records (created by loggers) to the appropriate destination.
# https://docs.python.org/2/howto/logging.html#useful-handlers
# ex: filename='my_logs.txt',filemode='a'
# Filters provide a finer grained facility for determining which log records to output.
# ex: level=logging.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s  - %(levelname)s - %(message)s',datefmt='%c'


# create logger
logger = logging.getLogger('disk_monitor')  # logger name
logger.setLevel(logging.DEBUG)                # Filter for logger

# create console handler and set level to debug
ch = logging.FileHandler('mydisk.log')                  # handler
ch.setLevel(logging.DEBUG)                    #  filter for handler

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter) # handler and formatter

# add ch to logger
logger.addHandler(ch)      # logger and handler

# Main


p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
disk_size = int(p2.communicate()[0].split()[4].split('%')[0])


if disk_size < 50:
	logger.info("The disk looks health at {}".format(disk_size))
elif disk_size < 70:
	logger.warning("The disk is getting filled up {}".format(disk_size))
elif disk_size < 80:
	logger.error("your application is sleeping now {}".format(disk_size))
elif disk_size < 100:
	logger.critical("your application is not working {}".format(disk_size))



