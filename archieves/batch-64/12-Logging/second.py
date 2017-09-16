#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter
# man date
# time.strftime()
import logging

logging.basicConfig(filename='myapp.log',filemode='a',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
	datefmt='%c',level=logging.DEBUG)

# file mode
# r - read a file.
# w - write to a file - if you have data in file it will be truncated to zero.
#                      - if not file it will be created
# a - append mode - add lines to the end of the file.

logging.debug("hey this is an debug message")
logging.info("hey this is an informational message")
logging.warning("hey this an warning message")
logging.error("hey this is an error message")
logging.critical("hey this is a critical message")

'''
challenges
* you can redirect our logmessage to a file or a console.
* logger name.
* we cannot login multiple logs to the same file.
* you might have to manage multiple files for multiple applications.

'''