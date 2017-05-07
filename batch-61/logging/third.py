#!/usr/bin/python
# cron - linux
# scheduler - window

import logging
from subprocess import Popen,PIPE

logging.basicConfig(filename="disk.log",filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',datefmt='%c')

# main
if __name__ == '__main__':
	
	# disk_size = $(df -h / | tail -n 1 | awk '{print $5}'|sed -e 's#%##g')
	#disk_size = int(raw_input("please enter the disk size:"))

	p1 = Popen(['df','-h','/'],stdout=PIPE)
	p2 = Popen(['tail','-n','-1'],stdin=p1.stdout,stdout=PIPE)
	output = p2.communicate()[0]
	disk_size = int(output.split()[4].split('%')[0])

	if disk_size < 50:
		logging.info("Your disk looks health at {}.".format(disk_size))
	elif disk_size < 70:
		logging.warning("your disk is getting filled up {}.".format(disk_size))
	elif disk_size < 80:
		logging.error("Your disk is puking errors at {}.".format(disk_size))
	else:
		logging.critical("your disk is dead. Please clean the logs - {}.".format(disk_size))


# challenges
# * logger name - root
# redirect to a file. (ex: syslog handler,email)
