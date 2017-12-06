#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date.
# linux -> crontab.
# window -> scheduler. 
# time.strftime()

import logging as l
from subprocess import Popen,PIPE

l.basicConfig(filename='my_disk.log',filemode='a',level=l.DEBUG,
			  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# modes
# r -> read mode -> you can only the read the file.
# w -> write mode -> you can write into a file.
# * if the file is having some content,truncates your file to zero.
# * if the file doesnt exits, we get a new file created and content into it.
# a -> append mode -> you can append into the file.

## 
# Main program
##

# #disk_size = int(raw_input("please enter the disk size:"))
# df -h / |tail -n 1|awk '{print $5}'|sed 's#%##'

if __name__ == '__main__':
	p1 = Popen(['df','-h','/'],stdout=PIPE)
	p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
	disk_size = int(p2.communicate()[0].split()[4].split('%')[0])

	if disk_size < 50:
		l.info("The disk looks health at {}.".format(disk_size))
	elif disk_size < 75:
		l.warning("The disk looks to give some warnings {}.".format(disk_size))
	elif disk_size < 85:
		l.error("The disk is puking some errors {}".format(disk_size))
	elif disk_size < 100:
		l.critical("The Application is sleeping now {}".format(disk_size))

'''
## challenges with logging files

1) we can only log to a file or max to a monitor.
2) using a logger with name is a big challenge.
3) this application logging is not for huge application.

'''
