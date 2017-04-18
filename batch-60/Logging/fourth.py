#!/usr/bin/python
# logging.basicConfig? or help(logging.basicConfig)
# logging.Formatter?
# man date or www.google.com -> man date
# time.strftime()

import logging
from subprocess import Popen,PIPE
import re

logging.basicConfig(filename="my_disk.log",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
	datefmt='%c')

# disk_size = $(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g')
#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]
disk_size = int(re.search('([0-9]+)%',output).group(1))
#print disk_size


if disk_size < 50:
	logging.info("The disk looks very healthy at {}.".format(disk_size))
elif disk_size < 70:
	logging.warning("The disk is getting filled up {}.".format(disk_size))
elif disk_size < 80:
	logging.error("The disk is puking errors {}.".format(disk_size))
elif disk_size < 99:
	logging.critical("your application is sleeping {}".format(disk_size))


# basicConfig
# save into a file or a console.
# no logger defined.

