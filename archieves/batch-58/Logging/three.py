#!/usr/bin/python
# l.basicConfig?
# l.Formatter?
# man date

import logging as l
from subprocess import Popen,PIPE
import re

l.basicConfig(filename='mydisk.log',filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=l.DEBUG,datefmt="%c")
# we can only send logs to disk,console.
# we are not able to handle the logger.

#a) Loggers expose the interface that application code directly uses.
# logger -> root 
#b) Handlers send the log records (created by loggers) to the appropriate destination.
# handler -> filename='mydisk.log',filemode='a'
#c) Filters provide a finer grained facility for determining which log records to output.
# filter -> level=l.DEBUG
#d) Formatters specify the layout of log records in the final output.
# formatter -> format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt="%c"


# disk info
# disk_size = int(raw_input("please enter the disk size:"))
# disk_size=$(df -h / | tail -n 1 | awk '{print $5}'|sed -e 's#%##g')

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]
#print output
disk_size = int(re.search('([0-9]+)%',output).group(1))

if disk_size < 60:
	l.info("The disk is healthy at {}.".format(disk_size))
elif disk_size < 75:
	l.warning("The disk is getting filled up {}".format(disk_size))
elif disk_size < 85:
	l.error("We are not able to write huge chunks at {}".format(disk_size))
elif disk_size < 100:
	l.critical("The disk is completly filled up at {}".format(disk_size))

