#!/usr/bin/python
# disk monitor

import logging as l
l.basicConfig(filename='disk_log.txt',filemode='a',level=l.DEBUG,
			  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			  datefmt='%c')

# modes
# r -> read -> you can only read the file.
# a -> append -> you can only append the contents to the file.
# w -> write -> you can write to the file.
#   -> if you dont have a file a new file will be created.
#   -> if you have a file with data,the file gets truncated to zero.

disk_size = int(raw_input("please enter  your disk size:"))

if disk_size < 60:
	l.info("Your disk looks healthy at {}.".format(disk_size))
elif disk_size < 80:
	l.warning("Buddy!! your disk is getting fat - {}.".format(disk_size))
elif disk_size < 90:
	l.error("Buddy!! you disk is feeling sick - {}.".format(disk_size))
elif disk_size < 99:
	l.critical("Buddy!! you disk is dead - {}.".format(disk_size))