#!/usr/bin/python
# crontab or scheduler.
 
import logging as l
from subprocess import Popen,PIPE
import re

l.basicConfig(filename="disk_log.txt",filemode="a",level=l.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')


# df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g'


# Main program
if __name__ == '__main__':
	#disk_size = int(raw_input("please enter the disk size to check ?"))
	p1 = Popen(["df","-h","/"],stdout=PIPE)
	p2 = Popen(["tail","-n","1"],stdin=p1.stdout,stdout=PIPE)
	output = p2.communicate()[0]
	disk_size = int(re.search('([0-9]+)%',output).group(1))

	if disk_size < 50:
		l.info("The disk looks health at {}".format(disk_size))
	elif disk_size < 70:
		l.warning("The disk is puking some warning at {}".format(disk_size))
	elif disk_size < 90:
		l.error("The disk seems to have some errors at {}".format(disk_size))
	elif disk_size < 100:
		l.critical("you disk is having some errors at {}".format(disk_size))
