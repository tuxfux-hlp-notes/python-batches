#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date.

import logging as l

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

if __name__ == '__main__':
	disk_size = int(raw_input("please enter the disk size:"))
	if disk_size < 50:
		l.info("The disk looks health at {}.".format(disk_size))
	elif disk_size < 75:
		l.warning("The disk looks to give some warnings {}.".format(disk_size))
	elif disk_size < 85:
		l.error("The disk is puking some errors {}".format(disk_size))
	elif disk_size < 100:
		l.critical("The Application is sleeping now {}".format(disk_size))
