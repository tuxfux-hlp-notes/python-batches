#!/usr/bin/python
# logging.basicConfig?
# logging.Formatter?
# man date or  time.strftime()
# scheduler - cron or scheduler - crontab
# https://docs.python.org/2/howto/logging-cookbook.html

import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.ERROR)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
