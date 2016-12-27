#!/usr/bin/python
# logging.basicConfig
# Messages on screen or file like object - StreamHandlers
# logging.Formatter
# man date/https://docs.python.org/2/library/time.html#time.strftime


import logging
logging.basicConfig(filename="disk.log",filemode='a',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%c')

# modes
# r - read mode - reading a file.
# w - write mode - write to a file. if file doesnot exist it should create it.
# if it exist truncates it to zero.
# a - append mode - appends contents to the file.

disk_size = input("plese enter the disk size:")

if disk_size < 40:
    logging.info("Your disk looks healthy at {}".format(disk_size))
elif disk_size < 60:
    logging.warning("Your disk is getting filled up {}".format(disk_size))
elif disk_size < 90:
    logging.error("your disk is stomach full. It going to burst out {}".format(disk_size))
elif disk_size < 100:
    logging.critical("your application is sleeping {}".format(disk_size))
