#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# shelx
# crontab or scheduler
# https://docs.python.org/2/library/subprocess.html
import logging as l
from subprocess import Popen,PIPE

if __name__ == '__main__':
		l.basicConfig(filename='disklog.txt',filemode='a',
				      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
				      level=l.DEBUG,
				      datefmt='%c')

# disk_value = $(df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g')
		#disk_value = int(raw_input("Please enter the disk size:"))
		p1 = Popen(['df','-h','/'],stdout=PIPE)
		p2 = Popen(['tail','-n','1'],stdin=p1.stdout,stdout=PIPE)
		disk_value = int(p2.communicate()[0].split()[-2].split('%')[0])

	
		if disk_value < 50:
			l.info("The disk looks healthy {}".format(disk_value))
		elif disk_value < 70:
			l.warning("Your disk is gettting fat {}".format(disk_value))
		elif disk_value < 80:
			l.error("Your disk is puking {}".format(disk_value))
		else:
			l.critical("your application has gone into coma - {}".format(disk_value))

'''
* logger name - multiple logs in same file create confusion.
* handlers - you can put logs only to files.
* we cannot push it to a larger audience.
'''