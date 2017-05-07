#!/usr/bin/python
import logging
from subprocess import Popen,PIPE
import re
import pdb


from logging.handlers import SMTPHandler
from creds import USER,PASS

# logger
logger = logging.getLogger('Alert - email')

# Handler
ch = SMTPHandler( ('smtp.gmail.com',465) ,'tuxfux.django@gmail.com' ,'tuxfux.hlp@gmail.com', 'Alert - Email ', credentials=(USER,PASS) ,secure= 'none')
ch.setLevel(logging.DEBUG)

# Logger and handler
logger.addHandler(ch)


if __name__ == '__main__':
	#disk_size = int(raw_input("please enter the disk size to check ?"))
	p1 = Popen(["df","-h","/"],stdout=PIPE)
	p2 = Popen(["tail","-n","1"],stdin=p1.stdout,stdout=PIPE)
	output = p2.communicate()[0]
	disk_size = int(re.search('([0-9]+)%',output).group(1))

	pdb.set_trace()
	if disk_size < 50:
		logger.info("The disk looks health at {}".format(disk_size))
	elif disk_size < 70:
		logger.warning("The disk is puking some warning at {}".format(disk_size))
	elif disk_size < 90:
		logger.error("The disk seems to have some errors at {}".format(disk_size))
	elif disk_size < 100:
		logger.critical("you disk is having some errors at {}".format(disk_size))


#emit()