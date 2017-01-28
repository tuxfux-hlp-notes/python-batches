#!/usr/bin/python
 
import logging as l

l.basicConfig(filename="disk_log.txt",filemode="a",level=l.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')


# Main program
if __name__ == '__main__':
	disk_size = int(raw_input("please enter the disk size to check ?"))

	if disk_size < 50:
		l.info("The disk looks health at {}".format(disk_size))
	elif disk_size < 70:
		l.warning("The disk is puking some warning at {}".format(disk_size))
	elif disk_size < 90:
		l.error("The disk seems to have some errors at {}".format(disk_size))
	elif disk_size < 100:
		l.critical("you disk is having some errors at {}".format(disk_size))