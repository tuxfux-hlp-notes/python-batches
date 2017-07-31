#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man data or time.strftime().
# https://docs.python.org/2/library/subprocess.html
# cronjob or scheduler

from subprocess import Popen,PIPE

import logging

logging.basicConfig(filename='my_logs.txt',filemode='a',level=logging.DEBUG,
	format='%(asctime)s - %(name)s  - %(levelname)s - %(message)s',datefmt='%c')

# Main
# to find out the information about my disk size.
# df -h / | tail -n 1 | awk '{print $5}'| sed -e 's#%##g'


#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
disk_size = int(p2.communicate()[0].split()[4].split('%')[0])


if disk_size < 50:
	logging.info("The disk looks health at {}".format(disk_size))
elif disk_size < 70:
	logging.warning("The disk is getting filled up {}".format(disk_size))
elif disk_size < 80:
	logging.error("your application is sleeping now {}".format(disk_size))
elif disk_size < 100:
	logging.critical("your application is not working {}".format(disk_size))


