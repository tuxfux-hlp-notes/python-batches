#!/usr/bin/python
# l.basicConfig?
# l.Formatter?
# man date or time.strftime()
# subprocess:https://docs.python.org/2/library/subprocess.html
# crontab or scheduler
# shelx

import logging as l
from subprocess import Popen,PIPE


l.basicConfig(filename='myapp.log',filemode='a',level=l.DEBUG,
			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			datefmt='%c')

# r -> read -> read the file.
# w -> write -> write the file.
# * if file doesnt exist , it gets created.
# * if file exists, it gets truncated to zero.
# a -> append -> append data to the end of the file.

# disk_space = $( df -h / | tail -n 1 | awk '{print $5}'|sed -e 's#%##g')

if __name__ == '__main__':
	#disk_size = int(raw_input("please enter the disk size:"))
	p1 = Popen(['df','-h','/'],stdout=PIPE)
	p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
	disk_size = int(p2.communicate()[0].split()[-2].split('%')[0])
	
	if disk_size < 50:
		l.info("Your disk looks healthy at {}.".format(disk_size))
	elif disk_size < 70:
		l.warning("seems our disk is incresing {}.Make sure you keep a track".format(disk_size))
	elif disk_size < 80:
		l.error("our application is about to choke at {}.".format(disk_size))
	elif disk_size < 99:
		l.critical("our application is down - {}".format(disk_size))