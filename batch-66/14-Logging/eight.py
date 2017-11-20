#!/usr/bin/python
# https://docs.python.org/2/howto/logging-cookbook.html

import logging

logger = logging.getLogger('simple_example')  # logger
logger.setLevel(logging.DEBUG)                # filter for the logger.
# create file handler which logs even debug messages
fh = logging.FileHandler('my_file.log')  # file handler
fh.setLevel(logging.DEBUG)               # filter for file handler.
# create console handler with a higher log level
ch = logging.StreamHandler()             # console handler
ch.setLevel(logging.ERROR)               # filter for console handler.
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)  # formatter and handler.
fh.setFormatter(formatter)  # formatter and handler.
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')