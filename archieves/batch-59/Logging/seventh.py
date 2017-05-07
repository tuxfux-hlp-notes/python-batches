#!/usr/bin/python
# Logging to mulitple destinations
import logging

# set up logging to file - see previous section for more details
# logger: root
logging.basicConfig(level=logging.DEBUG,   # filter
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', # formatter
                    datefmt='%m-%d %H:%M',  # formatter
                    filename='my_app.log',  # handler
                    filemode='w')           # handler
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler() # handler
console.setLevel(logging.INFO)    # filter for handler
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s') # formatter
# tell the handler to use this format
console.setFormatter(formatter)   # integrated formatter with console.
# add the handler to the root logger
logging.getLogger('').addHandler(console) ## integrating the root logger with console.

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Info message from logigng module.')

# Now, define a couple of other loggers which might represent areas in your
# application:
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Debug message from logger1.')
logger1.info('Info message from logger1.')
logger2.warning('warning message from logger2.')
logger2.error('Error message from logger2.')

