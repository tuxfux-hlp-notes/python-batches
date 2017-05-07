#!/usr/bin/python
# logging.basicConfig
# Messages on screen or file like object - StreamHandlers
# logging.Formatter
# man date/https://docs.python.org/2/library/time.html#time.strftime


import logging
from subprocess import Popen,PIPE
import re
# logging.basicConfig(filename="disk.log",filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# advanced logging
# logger : Loggers expose the interface that application code directly uses. - root.
# handlers : Handlers send the log records (created by loggers) to the appropriate destination.
# ex: filename="disk.log",filemode='a'
# Filters : Filters provide a finer grained facility for determining which log records to output.
# ex: level=logging.DEBUG
# Formatters specify the layout of log records in the final output.
# ex: format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# modes
# r - read mode - reading a file.
# w - write mode - write to a file. if file doesnot exist it should create it.
# if it exist truncates it to zero.
# a - append mode - appends contents to the file.

# Advanced Logging.

# create logger
# one of the challenges in basic config, where we cannot set up a logger or logger is root by default.
logger = logging.getLogger('disk Monitor')  # loggger
logger.setLevel(logging.DEBUG)              # Filter for your logger

# create console handler and set level to debug
# https://docs.python.org/2/howto/logging.html#useful-handlers
ch = logging.StreamHandler()  # handler - StreamHandler.
ch.setLevel(logging.DEBUG)    # filter for the handler.

# create formatter
# logging.Formatter?
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)  # handler and formatter

# add ch to logger
logger.addHandler(ch)       # logger and handlers

# lets make this more automated. I want to find out the disk / percentage.
# df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g'
# https://docs.python.org/2/library/subprocess.html
# put this script in crontab or scheduler

#disk_size = input("plese enter the disk size:")

p1 = Popen(['df','-h','/'],stdout=PIPE)
P2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
output = P2.communicate()[0]
disk_size = int(re.search('([0-9]+)%',output).group(1))


if disk_size < 40:
    logger.info("Your disk looks healthy at {}".format(disk_size))
elif disk_size < 60:
    logger.warning("Your disk is getting filled up {}".format(disk_size))
elif disk_size < 90:
    logger.error("your disk is stomach full. It going to burst out {}".format(disk_size))
elif disk_size < 100:
    logger.critical("your application is sleeping {}".format(disk_size))

