#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date or  time.strftime()
# scheduler - cron or scheduler - crontab

import logging
from subprocess import Popen,PIPE

logging.basicConfig(filename="diskapp.log",filemode='a',level=logging.DEBUG,
	format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s',
	datefmt = '%c')

# Main
# disk_size=$(df -h / | tail -n 1|awk '{print $5}'|sed -e 's#%##g')
#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(['df','-h','/'],stdout=PIPE)
p2 = Popen(['tail','-n','-1'],stdin=p1.stdout,stdout=PIPE)
output=p2.communicate()[0]
disk_size = int(output.split()[4].split('%')[0])


if __name__ == '__main__':
	if disk_size < 50:
		logging.info("The disk looks healthy at {}.".format(disk_size))
	elif disk_size < 70:
		logging.warning("Looks the disk is getting filledup at {}".format(disk_size))
	elif disk_size < 80:
		logging.error("Looks the disk is puking errors at {}".format(disk_size))
	elif disk_size < 99:
		logging.critical("My application is sleeping at {}".format(disk_size))

# basicConfig
# we can only log to a file or a console.
# in a single file - we want to rediret logs from multiple apps. - its going to be hard.
