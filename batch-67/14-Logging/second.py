#!/usr/bin/python
# l.basicConfig?
# l.Formatter?
# man date

import logging as l


l.basicConfig(filename='myapp.log',filemode='a',level=l.DEBUG,
			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			datefmt='%c')

# r -> read -> read the file.
# w -> write -> write the file.
# * if file doesnt exist , it gets created.
# * if file exists, it gets truncated to zero.
# a -> append -> append data to the end of the file.

l.debug("This is an debugging message.")
l.info("This is an information message.")
l.warning("this is an warning message.")
l.error("This is an error message.")
l.critical("This is an critical message.")


'''

The default level is WARNING, which means that only events of 
this level and above will be tracked, unless the logging 
package is configured to do otherwise.

WARNING:root:this is an warning message.
ERROR:root:This is an error message.
CRITICAL:root:This is an critical message.
'''