#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter
# man date
# time.strftime()
import logging

logging.basicConfig(filename='mydisk.log',filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
	datefmt='%c',level=logging.DEBUG)

# main
if __name__ == '__main__':
	disk_size = input("please enter your disk size:")
	if disk_size < 50:
		logging.info("your disk looks health at {}".format(disk_size))
	elif disk_size < 70:
		logging.warning("Your disk is getting fat at {}".format(disk_size))
	elif disk_size < 80:
		logging.error("your disk is puking errors {}".format(disk_size))
	else:
		logging.critical("your application has gone for a sleep {}".format(disk_size))

